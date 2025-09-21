"""
Simple test to validate our MLOps pipeline components work correctly.
This simulates what Airflow would do in the automated pipeline.
"""
import subprocess
import os
import sys

def test_pipeline():
    print("🧪 Testing MLOps Pipeline Components")
    
    # Change to project root
    os.chdir('../../')
    
    print("\n1️⃣ Testing Data Engineering...")
    try:
        result = subprocess.run([sys.executable, 'code/datasets/data_preprocessing.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Data Engineering: SUCCESS")
        else:
            print(f"❌ Data Engineering: FAILED - {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Data Engineering: ERROR - {e}")
        return False
    
    print("\n2️⃣ Testing Model Engineering...")
    try:
        result = subprocess.run([sys.executable, 'code/models/train_model.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Model Engineering: SUCCESS")
        else:
            print(f"❌ Model Engineering: FAILED - {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Model Engineering: ERROR - {e}")
        return False
    
    print("\n3️⃣ Testing Deployment...")
    try:
        # Test if containers are running
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if 'deployment-api' in result.stdout and 'deployment-app' in result.stdout:
            print("✅ Deployment: Containers are running")
        else:
            print("⚠️  Deployment: Containers not running, starting them...")
            os.chdir('code/deployment')
            subprocess.run(['docker-compose', 'up', '-d'])
            os.chdir('../../')
        
        # Test API endpoint
        import requests
        response = requests.get('http://localhost:8000/health')
        if response.status_code == 200:
            print("✅ Deployment: API is healthy")
        else:
            print("❌ Deployment: API health check failed")
            return False
            
    except Exception as e:
        print(f"❌ Deployment: ERROR - {e}")
        return False
    
    print("\n🎉 All pipeline components are working correctly!")
    print("The automated Airflow pipeline would run these same steps every 5 minutes.")
    return True

if __name__ == "__main__":
    success = test_pipeline()
    sys.exit(0 if success else 1)