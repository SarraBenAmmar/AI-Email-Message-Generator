"""
Database management for email sequences
"""
import sqlite3
import json
from typing import List, Optional

class DatabaseManager:
    def __init__(self, db_path: str = "email_sequences.db"):
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Initialize database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create sequences table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sequences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT NOT NULL,
                tone TEXT NOT NULL,
                audience TEXT NOT NULL,
                sequence_length INTEGER NOT NULL,
                channel TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                sequence_data TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Database initialized successfully")
    
    def save_sequence(self, prompt: str, tone: str, audience: str, sequence_length: int, channel: str, sequence_data: List[dict]):
        """Save generated sequence to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sequences (prompt, tone, audience, sequence_length, channel, sequence_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (prompt, tone, audience, sequence_length, channel, json.dumps(sequence_data)))
        
        conn.commit()
        conn.close()
        return cursor.lastrowid
    
    def get_recent_sequences(self, limit: int = 10):
        """Get recent generated sequences"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM sequences 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (limit,))
        
        sequences = cursor.fetchall()
        conn.close()
        
        return sequences

# Initialize database
db = DatabaseManager()