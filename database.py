import sqlite3
import os

DB_NAME = 'chatbot.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create packages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS packages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            destination TEXT,
            description TEXT,
            price TEXT,
            duration TEXT,
            category TEXT DEFAULT 'General'
        )
    ''')
    
    # Create learned Q&A table (user-taught facts)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learned_qa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            category TEXT DEFAULT 'general'
        )
    ''')
    
    # Create domain knowledge table (pre-loaded expert knowledge)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS domain_knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            category TEXT DEFAULT 'general',
            keywords TEXT
        )
    ''')
    
    # Check if packages are already inserted
    cursor.execute("SELECT COUNT(*) FROM packages")
    if cursor.fetchone()[0] == 0:
        # Insert initial Sri Lanka travel packages
        sample_packages = [
            ("Colombo City Tour", "Colombo", "Explore the commercial capital of Sri Lanka, including Galle Face Green, Viharamahadevi Park, and the bustling Pettah market.", "$40", "1 Day", "City Tour"),
            ("Kandy Heritage Experience", "Kandy", "Visit the sacred Temple of the Tooth Relic, stroll around Kandy Lake, and enjoy a cultural dance performance.", "$80", "2 Days", "Cultural"),
            ("Sigiriya Rock Fortress", "Sigiriya", "Climb the ancient rock fortress of Sigiriya, a UNESCO World Heritage site, and explore the ancient water gardens.", "$60", "1 Day", "Historical"),
            ("Galle Fort & South Coast", "Galle", "Discover the historic Dutch Fort in Galle, relax on Unawatuna beach, and visit a turtle hatchery.", "$100", "2 Days", "Beach & Heritage"),
            ("Yala Wildlife Safari", "Yala", "Experience a thrilling jeep safari in Yala National Park, famous for its high density of leopards, elephants, and diverse birdlife.", "$150", "2 Days", "Wildlife"),
            ("Nuwara Eliya Tea Country", "Nuwara Eliya", "Enjoy the cool climate of 'Little England', visit a tea plantation, and see Ramboda Falls.", "$120", "2 Days", "Nature"),
            ("Ella Adventure Trek", "Ella", "Hike to Ella Rock and Little Adam's Peak, visit the iconic Nine Arches Bridge, and enjoy breathtaking mountain views.", "$90", "2 Days", "Adventure"),
            ("Trincomalee Beach Retreat", "Trincomalee", "Relax on Nilaveli Beach, visit Koneswaram Temple, snorkel at Pigeon Island, and watch dolphins.", "$130", "3 Days", "Beach"),
            ("Anuradhapura Ancient Kingdom", "Anuradhapura", "Explore the ancient capital with sacred Bo Tree (Sri Maha Bodhi), Ruwanwelisaya Stupa, and Jetavanaramaya.", "$70", "1 Day", "Historical"),
            ("Polonnaruwa Heritage Trail", "Polonnaruwa", "Visit the medieval capital's ruins including the Gal Vihara rock temple, Royal Palace, and Parakrama Samudra lake.", "$65", "1 Day", "Historical"),
            ("Mirissa Whale Watching", "Mirissa", "Embark on an exciting whale and dolphin watching boat tour in the deep waters off Mirissa's coast.", "$85", "1 Day", "Wildlife"),
            ("Adam's Peak Pilgrimage", "Adam's Peak", "Climb the sacred Adam's Peak (Sri Pada) at dawn to witness the spectacular sunrise from the summit.", "$55", "1 Day", "Adventure"),
            ("Cultural Triangle Tour", "Sigiriya, Polonnaruwa, Dambulla", "A comprehensive 3-day tour covering Sigiriya Rock, Polonnaruwa ruins, and Dambulla Cave Temple.", "$220", "3 Days", "Cultural"),
            ("Southern Coast Explorer", "Galle, Mirissa, Tangalle", "Drive along the scenic southern coastline visiting Galle Fort, whale watching in Mirissa, and relaxing in Tangalle.", "$250", "4 Days", "Beach & Heritage"),
            ("Hill Country Rail Journey", "Kandy to Ella", "Experience one of the most scenic train rides in the world from Kandy to Ella through tea plantations and mountains.", "$75", "1 Day", "Nature"),
        ]
        cursor.executemany('''
            INSERT INTO packages (name, destination, description, price, duration, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_packages)
        
    conn.commit()
    conn.close()

def get_all_packages():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, destination, description, price, duration, category FROM packages")
    packages = cursor.fetchall()
    conn.close()
    return packages

def search_packages(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"%{keyword}%"
    cursor.execute('''
        SELECT name, destination, description, price, duration, category 
        FROM packages 
        WHERE name LIKE ? OR destination LIKE ? OR description LIKE ? OR category LIKE ?
    ''', (query, query, query, query))
    packages = cursor.fetchall()
    conn.close()
    return packages

def add_package(name, destination, description, price, duration, category='General'):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO packages (name, destination, description, price, duration, category)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, destination, description, price, duration, category))
    conn.commit()
    conn.close()

def delete_package(pkg_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM packages WHERE id = ?", (pkg_id,))
    conn.commit()
    conn.close()

def get_packages_with_ids():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, destination, description, price, duration, category FROM packages")
    packages = cursor.fetchall()
    conn.close()
    return packages

# --- Learned Q&A ---
def save_learned_qa(question, answer, category='general'):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM learned_qa WHERE question = ?", (question,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO learned_qa (question, answer, category) VALUES (?, ?, ?)", (question, answer, category))
        conn.commit()
    conn.close()

def get_learned_qa():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM learned_qa")
    qa_list = cursor.fetchall()
    conn.close()
    return qa_list

def get_learned_qa_with_ids():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, answer, category FROM learned_qa")
    qa_list = cursor.fetchall()
    conn.close()
    return qa_list

def delete_learned_qa(qa_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM learned_qa WHERE id = ?", (qa_id,))
    conn.commit()
    conn.close()

# --- Domain Knowledge ---
def add_domain_knowledge(question, answer, category='general', keywords=''):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO domain_knowledge (question, answer, category, keywords) VALUES (?, ?, ?, ?)",
                   (question, answer, category, keywords))
    conn.commit()
    conn.close()

def add_domain_knowledge_bulk(entries):
    """Add multiple domain knowledge entries at once.
    entries: list of (question, answer, category, keywords)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO domain_knowledge (question, answer, category, keywords) 
        VALUES (?, ?, ?, ?)
    ''', entries)
    conn.commit()
    conn.close()

def get_domain_knowledge():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM domain_knowledge")
    qa_list = cursor.fetchall()
    conn.close()
    return qa_list

def get_domain_knowledge_with_ids():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, answer, category, keywords FROM domain_knowledge")
    qa_list = cursor.fetchall()
    conn.close()
    return qa_list

def delete_domain_knowledge(dk_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM domain_knowledge WHERE id = ?", (dk_id,))
    conn.commit()
    conn.close()

def get_domain_knowledge_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM domain_knowledge")
    count = cursor.fetchone()[0]
    conn.close()
    return count

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
