import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import database


# STEMMER — Lightweight Porter-style suffix stripping

STEM_RULES = [
    (r'ies$', 'y'),    
    (r'ves$', 'f'),    
    (r'ses$', 's'),    
    (r'ches$', 'ch'),  
    (r'shes$', 'sh'),  
    (r'ness$', ''),    
    (r'ment$', ''),    
    (r'tion$', ''),   
    (r'sion$', ''),    
    (r'ing$', ''),     
    (r'ings$', ''),    
    (r'ful$', ''),     
    (r'ous$', ''),    
    (r'able$', ''),    
    (r'ible$', ''),   
    (r'ally$', ''),   
    (r'ly$', ''),      
    (r'ed$', ''),      
    (r'er$', ''),      
    (r'est$', ''),     
    (r'ity$', ''),     
    (r'ism$', ''),    
    (r'ist$', ''),     
    (r'ise$', ''),     
    (r'ize$', ''),     
    (r'ure$', ''),     
    (r's$', ''),       
]

def stem(word):
    if len(word) <= 3:
        return word
    for pattern, replacement in STEM_RULES:
        result = re.sub(pattern, replacement, word)
        if result != word and len(result) >= 3:
            return result
    return word


# STOPWORDS — Common words filtered from inputs

STOPWORDS = {
    'i', 'me', 'my', 'we', 'our', 'you', 'your', 'he', 'she', 'it', 'they',
    'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'shall', 'can', 'need', 'dare', 'ought',
    'am', 'and', 'but', 'or', 'nor', 'not', 'so', 'very', 'just',
    'about', 'above', 'after', 'again', 'all', 'also', 'any', 'because',
    'before', 'between', 'both', 'by', 'each', 'for', 'from', 'get',
    'got', 'here', 'how', 'if', 'in', 'into', 'more', 'most', 'no',
    'of', 'on', 'once', 'only', 'other', 'out', 'over', 'own', 'same',
    'some', 'still', 'such', 'than', 'that', 'then', 'there', 'these',
    'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up',
    'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why',
    'with', 'please', 'tell', 'know', 'want', 'like', 'going',
    # Common verbs that cause false TF-IDF matches
    'used', 'using', 'use', 'go', 'come', 'make', 'made', 'take',
    'taken', 'give', 'given', 'see', 'seen', 'find', 'found',
    'said', 'say', 'says', 'look', 'looking', 'try', 'trying',
    'think', 'thought', 'ask', 'asked', 'really', 'many', 'much',
    'lot', 'lots', 'things', 'thing', 'way', 'ways',
}

# SYNONYMS — Expand words to include BOTH original + synonym

SYNONYMS = {
    'trip': ['tour', 'trip'], 'vacation': ['holiday', 'vacation'],
    'journey': ['tour', 'journey'], 'travel': ['tour', 'travel'],
    'visit': ['tour', 'visit'], 'explore': ['tour', 'explore'],
    'cheap': ['budget', 'cheap'], 'affordable': ['budget', 'affordable'],
    'inexpensive': ['budget'], 'costly': ['expensive'], 'pricey': ['expensive'],
    'beach': ['coast', 'beach'], 'shore': ['coast', 'shore'],
    'seaside': ['coast', 'seaside'],
    'temple': ['religious', 'temple'], 'church': ['religious', 'church'],
    'mosque': ['religious', 'mosque'],
    'jungle': ['wildlife', 'jungle'], 'forest': ['wildlife', 'forest'],
    'animals': ['wildlife', 'animals'],
    'mountain': ['hill', 'mountain'], 'peak': ['hill', 'peak'],
    'hiking': ['trek', 'hiking'],
    'food': ['cuisine', 'food'], 'eat': ['cuisine', 'eat'],
    'restaurant': ['cuisine', 'restaurant'],
    'hotel': ['accommodation', 'hotel'], 'stay': ['accommodation', 'stay'],
    'lodge': ['accommodation'], 'hostel': ['accommodation', 'hostel'],
    'resort': ['accommodation', 'resort'],
    'rain': ['weather', 'rain'], 'climate': ['weather', 'climate'],
    'temperature': ['weather', 'temperature'],
    'money': ['currency', 'money'], 'cash': ['currency', 'cash'],
    'exchange': ['currency', 'exchange'],
    'safe': ['safety', 'safe'], 'secure': ['safety'], 'danger': ['safety', 'danger'],
    'cab': ['transport', 'cab'], 'taxi': ['transport', 'taxi'],
    'bus': ['transport', 'bus'], 'train': ['transport', 'train'],
    'tuk': ['transport', 'tuk'], 'drive': ['transport', 'drive'],
    'medicine': ['medical', 'medicine'], 'doctor': ['medical', 'doctor'],
    'hospital': ['medical', 'hospital'], 'pharmacy': ['medical', 'pharmacy'],
    'bar': ['nightlife', 'bar'], 'club': ['nightlife', 'club'],
    'party': ['nightlife', 'party'],
    'souvenir': ['shopping', 'souvenir'], 'buy': ['shopping', 'buy'],
    'gem': ['shopping', 'gem'], 'spice': ['shopping', 'spice'],
    'pack': ['packing', 'pack'], 'luggage': ['packing', 'luggage'],
    'festival': ['festivals', 'festival'], 'celebration': ['festivals', 'celebration'],
    'yoga': ['wellness', 'yoga'], 'ayurveda': ['wellness', 'ayurveda'],
    'surf': ['surfing', 'surf'], 'dive': ['diving', 'dive'],
    'snorkel': ['diving', 'snorkel'],
}


def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = text.split()
    processed = []
    for t in tokens:
        if t in STOPWORDS:
            continue
        
        stemmed = stem(t)
        if stemmed in STOPWORDS:
            continue
        
        syn_key = t if t in SYNONYMS else (stemmed if stemmed in SYNONYMS else None)
        if syn_key:
            for syn in SYNONYMS[syn_key]:
                s = stem(syn)
                if s not in processed:
                    processed.append(s)
            
            if stemmed not in processed:
                processed.append(stemmed)
        else:
            if stemmed not in processed:
                processed.append(stemmed)
    return ' '.join(processed)


def extract_raw_keywords(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = text.split()
    keywords = []
    for t in tokens:
        if t not in STOPWORDS and len(t) > 2:
            keywords.append(t)
            
            if t in SYNONYMS:
                for syn in SYNONYMS[t]:
                    if syn not in keywords:
                        keywords.append(syn)
    return set(keywords)


class ChatbotEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, max_df=0.95)
        self.knowledge_base = []
        self.corpus = []
        self.tfidf_matrix = None
        self.db_keywords = [] 
        self.train_model()

    def train_model(self):
        self.knowledge_base = []
        self.db_keywords = []

        # Static greetings
        static_facts = [
            ("hello", "Ayubowan! 🙏 Welcome to Sri Lanka Tours. How can I help you plan your trip?"),
            ("hi", "Ayubowan! 🙏 Welcome to Sri Lanka Tours. How can I help you plan your trip?"),
            ("hey", "Hey there! Ready to explore beautiful Sri Lanka?"),
            ("good morning", "Good morning! Ready to explore Sri Lanka?"),
            ("good evening", "Good evening! How can I assist you with Sri Lanka travel?"),
            ("thank you", "You are very welcome! Let me know if you need anything else."),
            ("thanks", "You're welcome! Happy to help with your Sri Lanka trip."),
            ("bye", "Goodbye! Have a safe and wonderful journey in Sri Lanka. 🌴"),
            ("goodbye", "Goodbye! Ayubowan! 🙏"),
            ("who are you", "I am CeylonBot — your AI-powered Sri Lanka Tour Planning Assistant. I can help you find tour packages, answer travel questions, and even learn new things from you!"),
            ("what can you do", "I can help you with Sri Lanka travel! Ask me about tour packages, destinations, weather, visa info, food, transport, and more. I also learn from our conversations!"),
            ("help", "I can assist you with: 🏖️ Tour packages, 🗺️ Destinations, 🌦️ Weather & best times to visit, 🍛 Local cuisine, 🚕 Transport options, 💰 Budget tips. Just ask!"),
        ]
        for q, a in static_facts:
            self.knowledge_base.append({'question': preprocess(q), 'answer': a, 'type': 'static'})
            self.db_keywords.append(set()) 

        # Package listing intents
        pkg_questions = [
            "what packages do you have", "show me tour packages",
            "i want to see holiday packages", "what are the available tours",
            "tour options in sri lanka", "destinations in sri lanka",
            "sri lanka tours", "list all packages", "available packages",
            "what tours can i book", "holiday deals",
        ]
        for q in pkg_questions:
            self.knowledge_base.append({'question': preprocess(q), 'answer': None, 'type': 'action_packages'})
            self.db_keywords.append({'package', 'tour', 'holiday', 'available'})

        # Package search intents (keyword-based)
        search_patterns = [
            "beach tours", "wildlife safari", "cultural tours",
            "adventure tours", "historical tours", "nature tours",
            "colombo tour", "kandy tour", "galle tour", "ella tour",
            "sigiriya tour", "yala tour", "trincomalee tour",
        ]
        for q in search_patterns:
            self.knowledge_base.append({'question': preprocess(q), 'answer': None, 'type': 'action_search'})
            self.db_keywords.append(set(q.lower().split()))

        # Load domain knowledge from DB (with keywords!)
        try:
            domain_qa = database.get_domain_knowledge_with_ids()
            for entry in domain_qa:
                q = entry[1]
                a = entry[2]
                keywords_str = entry[4] if len(entry) > 4 and entry[4] else ""
                kw_set = set(keywords_str.lower().split()) if keywords_str else set()
                self.knowledge_base.append({'question': preprocess(q), 'answer': a, 'type': 'domain'})
                self.db_keywords.append(kw_set)
        except Exception:
            pass

        # Load user-taught knowledge from DB
        try:
            learned_qa = database.get_learned_qa()
            for q, a in learned_qa:
                self.knowledge_base.append({'question': preprocess(q), 'answer': a, 'type': 'learned'})
                self.db_keywords.append(set())
        except Exception:
            pass

        # Fit TF-IDF
        self.corpus = [item['question'] for item in self.knowledge_base]
        if self.corpus:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)

    # Response builders
    def _format_packages(self, packages):
        if not packages:
            return "Sorry, I couldn't find any matching packages."
        response = ""
        for p in packages:
            cat = f" — <em>{p[5]}</em>" if len(p) > 5 and p[5] else ""
            response += (
                f"<div class='pkg-card'>"
                f"<b>📍 {p[0]}</b>{cat}<br>"
                f"<span class='pkg-dest'>📌 {p[1]}</span><br>"
                f"{p[2]}<br>"
                f"<span class='pkg-meta'>⏱ {p[4]} &nbsp;|&nbsp; 💰 {p[3]}</span>"
                f"</div>"
            )
        return response

    def _get_all_packages_response(self):
        packages = database.get_all_packages()
        if not packages:
            return "Currently, we don't have any packages available."
        return "Here are our Sri Lanka tour packages:<br><br>" + self._format_packages(packages)

    # Words too generic to use for package keyword search

    GENERIC_SEARCH_WORDS = {
        'sri', 'lanka', 'tour', 'package', 'trip', 'holiday', 'many',
        'much', 'best', 'good', 'nice', 'great', 'really', 'think',
        'say', 'ask', 'give', 'make', 'take', 'come', 'go', 'see',
        'look', 'find', 'show', 'thing', 'time', 'day', 'people',
        'way', 'new', 'old', 'big', 'small', 'long', 'short',
    }

    # Words that signal the user is asking about tours/packages (strict!)

    TOUR_INTENT_WORDS = {
        'tour', 'package', 'book', 'reserve', 'deal', 'offer',
        'itinerary', 'available',
    }

    def _search_packages_response(self, user_input):
        keywords = preprocess(user_input).split()
        search_keywords = [kw for kw in keywords if kw not in self.GENERIC_SEARCH_WORDS and len(kw) > 2]
        if not search_keywords:
            return None
        all_results = []
        for kw in search_keywords:
            results = database.search_packages(kw)
            for r in results:
                if r not in all_results:
                    all_results.append(r)
        if all_results:
            return "Here's what I found:<br><br>" + self._format_packages(all_results)
        return None

    def _has_tour_intent(self, user_input):
        words = set(preprocess(user_input).split())
        return bool(words & self.TOUR_INTENT_WORDS)


    # MULTI-SIGNAL SCORING — Combines TF-IDF with keyword matching
   
    def _compute_keyword_score(self, user_input, idx):
        if idx >= len(self.db_keywords) or not self.db_keywords[idx]:
            return 0.0
        input_keywords = extract_raw_keywords(user_input)
        db_kws = self.db_keywords[idx]
        if not db_kws:
            return 0.0
        
        matches = input_keywords & db_kws
        return len(matches) / max(len(db_kws), 1)

    def _compute_combined_score(self, tfidf_score, keyword_score):
        
        return (0.6 * tfidf_score) + (0.4 * keyword_score)

    def _validate_match(self, processed_input, matched_question, keyword_score):
        input_words = set(processed_input.split())
        match_words = set(matched_question.split())
        overlap = input_words & match_words
        meaningful_overlap = {w for w in overlap if len(w) > 2}

        
        if len(meaningful_overlap) >= 1:
            return True
        
        if keyword_score >= 0.3:
            return True
        return False

    def get_response(self, user_input):
        if not self.corpus:
            return {"text": "My knowledge base is empty.", "emotion": "confused", "learning": False}

        processed_input = preprocess(user_input)
        input_vec = self.vectorizer.transform([processed_input])
        similarities = cosine_similarity(input_vec, self.tfidf_matrix)

        scores = similarities[0]

        
        combined_scores = np.zeros(len(scores))
        for i in range(len(scores)):
            kw_score = self._compute_keyword_score(user_input, i)
            combined_scores[i] = self._compute_combined_score(scores[i], kw_score)

        sorted_indices = combined_scores.argsort()[::-1]

        # Dynamic threshold: shorter inputs need higher confidence
        input_word_count = len(processed_input.split())
        if input_word_count <= 1:
            THRESHOLD = 0.30 
        elif input_word_count <= 3:
            THRESHOLD = 0.38
        else:
            THRESHOLD = 0.35 

        # Try the top 5 matches (more candidates = better chance of a good match)
        for idx in sorted_indices[:5]:
            combined = combined_scores[idx]
            tfidf = scores[idx]
            kw_score = self._compute_keyword_score(user_input, idx)

            if combined < THRESHOLD:
                break

            matched = self.knowledge_base[idx]
            matched_q = matched['question']

            
            if matched['type'] == 'static' and len(matched_q.split()) <= 2:
                return {"text": matched['answer'], "emotion": "happy", "learning": False}

            
            if not self._validate_match(processed_input, matched_q, kw_score):
                continue 

            if matched['type'] == 'action_packages':
                if self._has_tour_intent(user_input):
                    return {"text": self._get_all_packages_response(), "emotion": "happy", "learning": False}
                else:
                    continue  
            elif matched['type'] == 'action_search':
                if self._has_tour_intent(user_input):
                    result = self._search_packages_response(user_input)
                    if result:
                        return {"text": result, "emotion": "happy", "learning": False}
                    return {"text": self._get_all_packages_response(), "emotion": "happy", "learning": False}
                else:
                    continue  
            else:
                return {"text": matched['answer'], "emotion": "happy", "learning": False}

        # Fallback: only try package search if the question has tour-related intent
        if self._has_tour_intent(user_input):
            search_result = self._search_packages_response(user_input)
            if search_result:
                return {"text": search_result, "emotion": "happy", "learning": False}

        # Nothing found — ask user to teach
        return {
            "text": "🤔 I'm not sure how to answer that yet. Could you teach me? Type the answer you'd expect, and I'll remember it!",
            "emotion": "confused",
            "learning": True
        }

    def learn(self, question, answer):
        database.save_learned_qa(question, answer)
        self.train_model()
        return {
            "text": "✅ Thank you! I've learned that. Ask me again anytime! What else can I help with?",
            "emotion": "happy",
            "learning": False
        }
