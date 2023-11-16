import instaloader
import time
from tqdm import tqdm
import feedparser
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from colorama import Fore, Back, Style, init

init()

L = instaloader.Instaloader()

nltk.download('punkt')
nltk.download('stopwords')


def print_motd() :
    print("\033[34m" + r"""
        ,--.-,,-,--,   ,---.        ,-,--.  ,--.-,,-,--,,--.--------.   ,---.          _,---.                ,---.             ___   
    /==/  /|=|  | .--.'  \     ,-.'-  _\/==/  /|=|  /==/,  -   , -\.--.'  \     _.='.'-,  \  .-.,.---.  .--.'  \     .-._ .'=.'\  
    |==|_ ||=|, | \==\-/\ \   /==/_ ,_.'|==|_ ||=|, \==\.-.  - ,-./\==\-/\ \   /==.'-     / /==/  `   \ \==\-/\ \   /==/ \|==|  | 
    |==| ,|/=| _| /==/-|_\ |  \==\  \   |==| ,|/=| _|`--`\==\- \   /==/-|_\ | /==/ -   .-' |==|-, .=., |/==/-|_\ |  |==|,|  / - | 
    |==|- `-' _ | \==\,   - \  \==\ -\  |==|- `-' _ |     \==\_ \  \==\,   - \|==|_   /_,-.|==|   '='  /\==\,   - \ |==|  \/  , | 
    |==|  _     | /==/ -   ,|  _\==\ ,\ |==|  _     |     |==|- |  /==/ -   ,||==|  , \_.' )==|- ,   .' /==/ -   ,| |==|- ,   _ | 
    |==|   .-. ,\/==/-  /\ - \/==/\/ _ ||==|   .-. ,\     |==|, | /==/-  /\ - \==\-  ,    (|==|_  . ,'./==/-  /\ - \|==| _ /\   | 
    /==/, //=/  |\==\ _.\=\.-'\==\ - , //==/, //=/  |     /==/ -/ \==\ _.\=\.-'/==/ _  ,  //==/  /\ ,  )==\ _.\=\.-'/==/  / / , / 
    `--`-' `-`--` `--`         `--`---' `--`-' `-`--`     `--`--`  `--`        `--`------' `--`-`--`--' `--`        `--`./  `--`  
    """ + "\033[0m")

def extract_keywords(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    return set(words)

def get_news_feed(themes, wordlist_name, pdf_name):
    keywords_list = set()
    pdf_file = f'{pdf_name}.pdf'
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    story = []
    link_style = ParagraphStyle(name='LinkStyle', parent=getSampleStyleSheet()['Normal'])
    link_style.textColor = colors.blue
    link_style.alignment = 1
    link_style.leading = 12

    for theme in themes:
        rss_url = f"https://news.google.com/rss/search?q={theme}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(rss_url)

        if feed.get('entries'):
            for entry in feed.entries:
                print(f"Title: {entry.title}")
                print(f"Link: {entry.link}")
                print(f"Publication Date: {entry.published}")
                title_keywords = extract_keywords(entry.title)
                description_keywords = extract_keywords(entry.description)
                keywords_list.update(title_keywords)
                keywords_list.update(description_keywords)
                title_text = f"Title: {entry.title}"
                story.append(Paragraph(title_text, getSampleStyleSheet()["Title"]))
                link_text = f'<a href="{entry.link}">lien</a>'
                story.append(Paragraph(link_text, link_style))
                story.append(Spacer(1, 0.2 * inch))
        else:
            print(f"No news found for the theme '{theme}'.")
    doc.build(story)

    with open(f'{wordlist_name}.txt', 'w') as file:
        for keyword in keywords_list:
            file.write(f"{keyword}\n")
def download_posts_by_hashtag(hashtag, count, number):
    try:
        for post in tqdm(L.get_hashtag_posts(hashtag), total=number, desc=f"Downloading #{hashtag}"):
            if count < number:
                L.download_post(post, target=hashtag)
                count += 1
            else:
                break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return count

def main(number):
    count = 0
    with open("keywords.txt", "r") as file:
        hashtags = [line.strip() for line in file.readlines()]
        for hashtag in hashtags:
            count = download_posts_by_hashtag(hashtag, count, number)
            time.sleep(5)
            print(f"Total posts downloaded for {hashtag}: {count}")
            if count >= number:
                count = 0

while True:
    print_motd()
    print("\n1. Search for posts via keyword")
    print("2. RSS news on multiple keywords + create a wordlist from specified RSS news")
    print("3. Exit")

    choice = input("\nChoice: ")

    if choice == '1':
        print(Back.YELLOW + Fore.RED + "\nMake sure you have created a keywords.txt file\n" + Style.RESET_ALL)
        number = int(input("Number of posts wanted per keyword: "))
        main(number)
        print(Back.BLUE + Fore.BLACK + "Files containing posts by keyword have been generated" + Style.RESET_ALL)
    elif choice == '2':
        theme_input = input("Enter themes for RSS news (separated by commas): ")
        themes = [theme.strip() for theme in theme_input.split(',')]
        wordlist_name = str(input("Choose a name for the wordlist: "))
        pdf_name = str(input("Choose a name for the PDF RSS news: "))
        get_news_feed(themes, wordlist_name, pdf_name)
        print(Back.BLUE + Fore.BLACK + f"The wordlist {wordlist_name}.txt containing keyword has been generated" + Style.RESET_ALL)
        print(Back.BLUE + Fore.BLACK + f"The PDF {pdf_name}.pdf containing RSS news has been generated" + Style.RESET_ALL)
    elif choice == '3':
        print("Exiting the script.")
        break
    else:
        print(Back.YELLOW + Fore.RED + "Invalid choice. Please select a valid option (1, 2, or 3)." + Style.RESET_ALL)
