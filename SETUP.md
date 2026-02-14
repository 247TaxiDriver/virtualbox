# כיצד להוריד את הפרויקט למחשב שלך | How to Download This Project to Your Computer

## עברית | Hebrew

### דרישות מוקדמות
1. **התקנת Git**: ודא ש-Git מותקן על המחשב שלך
   - Windows: הורד מ-[git-scm.com](https://git-scm.com/download/win)
   - Mac: התקן דרך Homebrew: `brew install git` או הורד מ-[git-scm.com](https://git-scm.com/download/mac)
   - Linux: `sudo apt-get install git` (Ubuntu/Debian) או `sudo yum install git` (CentOS/RHEL)

2. **חשבון GitHub** (אופציונלי אך מומלץ)
   - אם אין לך חשבון, צור אחד ב-[github.com](https://github.com)

### שלבי ההורדה

#### שיטה 1: שיבוט הריפוזיטורי (מומלץ)

1. **פתח את Terminal או Command Prompt**
   - Windows: חפש "cmd" או "PowerShell" בתפריט Start
   - Mac: פתח Terminal מ-Applications > Utilities
   - Linux: השתמש בטרמינל שלך

2. **נווט לתיקיה שבה תרצה לשמור את הפרויקט**
   ```bash
   cd C:\Projects  # Windows
   cd ~/Projects   # Mac/Linux
   ```

3. **שבט את הריפוזיטורי**
   ```bash
   git clone https://github.com/247TaxiDriver/virtualbox.git
   ```

4. **היכנס לתיקיית הפרויקט**
   ```bash
   cd virtualbox
   ```

5. **אמת שההורדה הצליחה**
   ```bash
   git status
   ls  # או dir בWindows
   ```

#### שיטה 2: הורדה כקובץ ZIP (פשוט יותר)

1. עבור ל-https://github.com/247TaxiDriver/virtualbox
2. לחץ על כפתור "Code" הירוק
3. בחר "Download ZIP"
4. חלץ את קובץ ה-ZIP לתיקיה הרצויה

### עדכון הקוד (לאחר השיבוט)

כדי לקבל את העדכונים האחרונים:
```bash
cd virtualbox
git pull origin main
```

### בניית הפרויקט

פרויקט VirtualBox מורכב ודורש תלויות רבות. עיין ב:
- [הוראות בנייה רשמיות](https://www.virtualbox.org/wiki/Build_instructions)
- קובץ README.md בתיקייה

### פתרון בעיות

- **שגיאת "git: command not found"**: Git לא מותקן. התקן אותו תחילה.
- **שגיאת גישה**: וודא שיש לך גישה לריפוזיטורי או שהוא ציבורי.
- **קובץ גדול מדי**: הפרויקט גדול (~1.2GB). וודא שיש מספיק מקום פנוי.

---

## English

### Prerequisites
1. **Install Git**: Make sure Git is installed on your computer
   - Windows: Download from [git-scm.com](https://git-scm.com/download/win)
   - Mac: Install via Homebrew: `brew install git` or download from [git-scm.com](https://git-scm.com/download/mac)
   - Linux: `sudo apt-get install git` (Ubuntu/Debian) or `sudo yum install git` (CentOS/RHEL)

2. **GitHub Account** (optional but recommended)
   - If you don't have one, create one at [github.com](https://github.com)

### Download Steps

#### Method 1: Clone the Repository (Recommended)

1. **Open Terminal or Command Prompt**
   - Windows: Search for "cmd" or "PowerShell" in Start menu
   - Mac: Open Terminal from Applications > Utilities
   - Linux: Use your terminal

2. **Navigate to where you want to save the project**
   ```bash
   cd C:\Projects  # Windows
   cd ~/Projects   # Mac/Linux
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/247TaxiDriver/virtualbox.git
   ```

4. **Enter the project directory**
   ```bash
   cd virtualbox
   ```

5. **Verify the download succeeded**
   ```bash
   git status
   ls  # or dir on Windows
   ```

#### Method 2: Download as ZIP File (Simpler)

1. Go to https://github.com/247TaxiDriver/virtualbox
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to your desired location

### Updating the Code (After Cloning)

To get the latest updates:
```bash
cd virtualbox
git pull origin main
```

### Building the Project

VirtualBox is a complex project requiring many dependencies. See:
- [Official build instructions](https://www.virtualbox.org/wiki/Build_instructions)
- README.md file in the directory

### Common Issues

- **"git: command not found" error**: Git is not installed. Install it first.
- **Permission error**: Make sure you have access to the repository or it's public.
- **File too large**: The project is large (~1.2GB). Ensure you have enough free space.

---

## Additional Resources

- **VirtualBox Documentation**: https://docs.oracle.com/en/virtualization/virtualbox/
- **Build Instructions**: https://www.virtualbox.org/wiki/Build_instructions
- **Development Documentation**: https://www.virtualbox.org/wiki/Technical_documentation
- **Fork Information**: See [FORK_INFO.md](./FORK_INFO.md) for details about this fork

## System Requirements for Building

- **Disk Space**: At least 10GB free space
- **RAM**: 4GB minimum, 8GB recommended
- **OS**: Windows 10+, macOS 10.15+, or Linux (various distributions)
- **Build Tools**: See official build instructions for specific requirements per OS
