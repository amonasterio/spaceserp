import json

class OrganicResult:
    def __init__(self, position, page, domain, link, title, description):
        self.position = position
        self.page = page
        self.domain = domain
        self.link = link
        self.title = title
        self.description = description

    def __repr__(self):
        return (f"OrganicResult(position={self.position}, page={self.page}, domain='{self.domain}', "
                f"link='{self.link}', title='{self.title}', description='{self.description}')")

    def is_domain(self, domain_to_check):
        """Checks if the domain matches the specified domain name."""
        return self.domain == domain_to_check
    

# Function to parse the JSON file and create OrganicResult instances
def parse_organic_results(data_json):
    # Extract organic results if the structure matches
    organic_results_data = data_json.get('organic_results', [])
    organic_results = []
    for result in organic_results_data:
        organic_result = OrganicResult(
            position=result.get('position'),
            page=result.get('page'),
            domain=result.get('domain'),
            link=result.get('link'),
            title=result.get('title'),
            description=result.get('description')
        )
        organic_results.append(organic_result)

    return organic_results


# Function to parse the JSON file and create OrganicResult instances
def parse_organic_results_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    return parse_organic_results(data)
    

'''
# Usage example
organic_results = parse_organic_results_json_file('test.json')

# Display the results
for result in organic_results:
    print(result)
'''