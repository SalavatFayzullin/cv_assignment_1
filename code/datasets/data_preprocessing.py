import pandas as pd
from sklearn.model_selection import train_test_split
import os

try:
    print("Starting data processing...")
    os.makedirs('data/processed', exist_ok=True)
    
    # Load data
    df = pd.read_csv('data/raw/titanic.csv')
    print(f"Loaded data: {df.shape}")
    
    # Clean data
    df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # Split data
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save processed data
    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)
    
    train_df.to_csv('data/processed/train.csv', index=False)
    test_df.to_csv('data/processed/test.csv', index=False)
    
    print("Data processed and saved successfully!")
    
except Exception as e:
    print(f"Error: {e}")