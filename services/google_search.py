from googlesearch import search
import requests
from bs4 import BeautifulSoup
from core.logger import get_logger

logger = get_logger()

def search_google(query, num_results=3):
    """
    Search Google and return relevant snippets
    """
    try:
        results = []
        search_query = f"medical {query}"
        
        for url in search(search_query, num_results=num_results, lang="en"):
            try:
                response = requests.get(url, timeout=5, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                })
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    for script in soup(["script", "style"]):
                        script.decompose()
                    
                    text = soup.get_text()
                    lines = (line.strip() for line in text.splitlines())
                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                    text = ' '.join(chunk for chunk in chunks if chunk)
                    
                    if len(text) > 200:
                        results.append({
                            'url': url,
                            'content': text[:1000]
                        })
                        
            except Exception as e:
                logger.warning(f"Failed to fetch {url}: {str(e)}")
                continue
        
        return results
        
    except Exception as e:
        logger.error(f"Google search failed: {str(e)}")
        return []
