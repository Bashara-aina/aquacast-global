"""Check if Favorita dataset is properly downloaded."""
from pathlib import Path

def check_favorita_data():
    """Verify all required Favorita files are present."""
    raw_dir = Path(__file__).parent.parent / "raw"
    
    required_files = [
        "train.csv",
        "items.csv", 
        "stores.csv",
        "oil.csv"
    ]
    
    print("Checking Favorita dataset...")
    print(f"Looking in: {raw_dir.absolute()}\n")
    print("=" * 60)
    
    missing = []
    total_size = 0
    
    for filename in required_files:
        filepath = raw_dir / filename
        if filepath.exists():
            size_mb = filepath.stat().st_size / (1024 * 1024)
            total_size += size_mb
            print(f"✅ {filename:20s} ({size_mb:8,.1f} MB)")
        else:
            print(f"❌ {filename:20s} MISSING")
            missing.append(filename)
    
    print("=" * 60)
    
    if missing:
        print(f"\n❌ Missing {len(missing)} file(s): {', '.join(missing)}")
        print("\nTo download:")
        print("1. Go to: https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting/data")
        print("2. Accept competition rules")
        print("3. Run: kaggle competitions download -c favorita-grocery-sales-forecasting -p data\\raw\\")
        return False
    else:
        print(f"\n✅ All files present!")
        print(f"Total size: {total_size:,.1f} MB")
        return True

if __name__ == "__main__":
    check_favorita_data()
