# ChatGPT AI Search Scraper - Bright Data API
# Simple Python implementation
# Install: pip install requests colorama
# Run with: python chatgpt_scraper.py

import requests
import json
import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# ========================================
# CONFIGURATION
# ========================================
API_TOKEN = 'BRIGHT_DATA_API_KEY'  # Get from Account Settings -> API Key
DATASET_ID = 'gd_m7aof0k82r803d5bjm'  # Fixed ChatGPT AI Search dataset ID

# ========================================
# SAMPLE SEARCH EXAMPLES (Reduced to 3 for faster results)
# ========================================
SAMPLE_SEARCHES = [
    {
        "url": "https://chatgpt.com/",
        "prompt": "Top hotels in New York",
        "country": ""
    },
    {
        "url": "https://chatgpt.com/",
        "prompt": "What are the biggest business trends to watch in the next five years?",
        "country": ""
    },
    {
        "url": "https://chatgpt.com/",
        "prompt": "Best practices for remote team management",
        "country": ""
    }
]

# ========================================
# CORE FUNCTIONS
# ========================================

def api_request(method, path, data=None):
    """Simple API request function"""
    url = f"https://api.brightdata.com{path}"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    try:
        if method == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method == 'GET':
            response = requests.get(url, headers=headers)
        
        if response.status_code >= 400:
            raise Exception({
                'statusCode': response.status_code,
                'error': 'API request failed',
                'rawResponse': response.text
            })
        
        return response.text
    
    except requests.exceptions.RequestException as e:
        raise Exception({
            'error': 'Request failed',
            'details': str(e)
        })

# ========================================
# MAIN SCRAPER FUNCTION
# ========================================

def search_chatgpt(search_inputs):
    """Main ChatGPT search function"""
    try:
        print(f"{Fore.CYAN}{Style.BRIGHT}🤖 Starting ChatGPT AI Search...")
        print(f"{Fore.BLUE}📝 Searching {len(search_inputs)} prompts")
        
        # Display the raw JSON being sent
        print(f"{Fore.LIGHTBLACK_EX}📤 Sending JSON body:")
        print(f"{Fore.LIGHTBLACK_EX}{json.dumps(search_inputs, indent=2)}")
        
        # 1. Trigger collection - send search_inputs as raw JSON body
        trigger_path = f"/datasets/v3/trigger?dataset_id={DATASET_ID}"
        raw_response = api_request('POST', trigger_path, search_inputs)
        response_data = json.loads(raw_response)
        snapshot_id = response_data['snapshot_id']
        print(f"{Fore.GREEN}✅ Search started! Snapshot ID: {snapshot_id}")

        # 2. Wait for completion
        print(f"{Fore.YELLOW}⏳ Processing searches...")
        status = 'running'
        attempts = 0
        max_attempts = 60  # 5 minutes max wait
        
        while status != 'ready' and attempts < max_attempts:
            time.sleep(5)  # Wait 5 seconds
            progress_response = api_request('GET', f"/datasets/v3/progress/{snapshot_id}")
            progress = json.loads(progress_response)
            status = progress['status']
            attempts += 1
            
            print(f"{Fore.LIGHTBLACK_EX}📊 Status: {status} ({attempts}/{max_attempts})")
            
            if status == 'failed':
                raise Exception('Search failed')

        if status != 'ready':
            raise Exception('Search timeout - taking longer than expected')

        # 3. Download results
        print(f"{Fore.BLUE}⬇️ Downloading AI responses...")
        downloaded_results = api_request('GET', f"/datasets/v3/snapshot/{snapshot_id}")
        print(f"{Fore.GREEN}{Style.BRIGHT}🎉 Success! Downloaded results")

        return downloaded_results

    except Exception as error:
        error_msg = str(error) if isinstance(error, str) else json.dumps(error, indent=2)
        print(f"{Fore.RED}{Style.BRIGHT}❌ Error: {Fore.RED}{error_msg}")
        raise

# ========================================
# HELPER FUNCTIONS
# ========================================

def create_search(prompt, country=""):
    """Create a custom search input"""
    return {
        "url": "https://chatgpt.com/",
        "prompt": prompt,
        "country": country
    }

def save_results(data, filename=None):
    """Save results to file"""
    # Generate filename with timestamp if not provided
    if not filename:
        timestamp = datetime.now().isoformat().replace(':', '-').replace('.', '-')
        filename = f"chatgpt_results_{timestamp}.json"

    # Save raw response
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"{Fore.GREEN}💾 Results saved to {Style.BRIGHT}{filename}{Style.RESET_ALL}")

# ========================================
# MAIN FUNCTION
# ========================================

def main():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}🌟 ChatGPT AI Search Scraper")
    print(f"{Fore.MAGENTA}=============================")
    
    # Validate API token
    if API_TOKEN == 'YOUR_API_TOKEN_HERE':
        print(f"{Fore.RED}{Style.BRIGHT}❌ Please update your API_TOKEN!")
        print(f"{Fore.YELLOW}📖 Get it from: Account Settings -> API Token")
        return

    try:
        # Example 1: Use sample searches (sent as raw JSON body)
        print(f"{Fore.CYAN}\n📋 Running sample searches...")
        sample_results = search_chatgpt(SAMPLE_SEARCHES)
        save_results(sample_results)

        # Example 2: Custom single search
        # custom_search = [create_search("Best programming languages to learn in 2024")]
        # custom_results = search_chatgpt(custom_search)
        # save_results(custom_results, 'custom_search.json')

        # Example 3: Multiple custom searches
        # multiple_searches = [
        #     create_search("Climate change solutions"),
        #     create_search("AI ethics guidelines"),
        #     create_search("Sustainable business practices")
        # ]
        # multi_results = search_chatgpt(multiple_searches)
        # save_results(multi_results, 'multiple_searches.json')

        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨ All done! Check the saved JSON file for results.")
        
    except Exception as error:
        error_msg = str(error)
        print(f"{Fore.RED}{Style.BRIGHT}💥 Failed: {Fore.RED}{error_msg}")

# ========================================
# ADDITIONAL EXAMPLES
# ========================================

def quick_search(prompt):
    """Quick search function for single prompts"""
    search_input = [create_search(prompt)]
    return search_chatgpt(search_input)

def batch_search(prompts):
    """Batch search function for multiple prompts"""
    search_inputs = [create_search(prompt) for prompt in prompts]
    return search_chatgpt(search_inputs)

# Run if executed directly
if __name__ == "__main__":
    main()