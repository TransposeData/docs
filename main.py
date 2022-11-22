import secrets

PYTHON_REQUEST_TEMPLATE = """
import requests

url = "{}"
sql_query = \"\"\"{}\"\"\"

headers = {{
    'Content-Type': 'application/json',
    'X-API-KEY': '<YOUR API KEY>',
}}

response = requests.post(url,
    headers=headers,
    json={{
        'sql': sql_query
    }}
)

print(response.text)
"""

CURL_REQUEST_TEMPLATE = """
curl --request POST \\
     --data {{'sql': '{}'}} \\
     --url '{}' \\
     --header 'accept: application/json' \\
     --header 'x-api-key: <YOUR API KEY>'
"""

JS_REQUEST_TEMPLATE = """
const fetch = require('node-fetch');

const url = '{}';
const sql_query = '{}';

const headers = {{
    'Content-Type': 'application
"""

class TransposeDocsSQL:

    def __init__(self, endpoint, sql, method):
        self.sql = sql
        self.endpoint = endpoint
        self.api_key = '<YOUR API KEY>'
        self.method = method
        self.unique_identifier = secrets.token_hex(8)

    def _get_sql_entry(self):
        """
        Returns a Fenced Code Block with SQL syntax highlighting, where the body of the block is the SQL query.
        """
        return  ('``` { .sql #' + self._get_sql_entry_id() + ' title="SQL Query" }\n' +
                f'{self.sql}\n' +
                 '```') 

    def _get_python_code(self):
        """
        Returns a Fenced Code Block with Python syntax highlighting, where the body of the block is the Python code.
        """
        code_snippet = PYTHON_REQUEST_TEMPLATE.format(self.endpoint, self.sql)
        return ('=== "Python"\n' +
                '    ```py\n'    +
                '{}\n'           +
                '    ```').format(self._indent(code_snippet))

    def _get_node_code(self):
        """
        TODO: Implement this properly
        """
        return '=== "Node"\n\t```js\n\tconsole.log("Hello World")\n\t```'

    def _get_curl_code(self):
        """
        Returns a Fenced Code Block with Bash syntax highlighting, where the body of the block is the curl command.
        """
        code_snippet = CURL_REQUEST_TEMPLATE.format(self.sql, self.endpoint)
        return ('=== "Curl"\n'  +
                '    ```bash\n' + 
                '{}\n'          + 
                '    ```').format(self._indent(code_snippet))

    def _get_api_multilang(self):
        """
        Created tabbed view of various ways to call this API.
        """
        return '\n'.join([
            self._get_python_code(),
            self._get_node_code(),
            self._get_curl_code(),
        ])
    
    def _get_sql_entry_id(self):
        return f'{self.unique_identifier}_sql_entry'

    def _get_query_output_id(self):
        return f'{self.unique_identifier}_query_output'

    def _get_run_query_button(self):
        request_to_issue = f'issueRequest(event, \'{self._get_sql_entry_id()}\', \'{self._get_query_output_id()}\')'
        return f'<a class="md_button run_query_button" onclick="{request_to_issue}">Run Query</a>'

    def _get_response_box(self):
        return ('```{ .json #' + self._get_query_output_id() + ' title="Response" }\n' +
                '{\n    "data": [],\n    "error": null,\n    "status": 200\n}\n```')

    def _indent(self, string):
        return '\n'.join(['    ' + line for line in string.split('\n')])

    def _admonish(self, string):
        return ('!!! example "Give it a go!"\n' + 
                self._indent(string))

    def __call__(self):
        return self._admonish('\n'.join([
            self._get_sql_entry(),
            self._get_api_multilang(),
            self._get_run_query_button(),
            self._get_response_box(),
        ]))

class TransposeDocsRest:
    pass

def define_env(env):

    @env.macro
    def transpose_sql_endpoint(endpoint: str, default_sql: str, method: str):
        output_string = TransposeDocsSQL(endpoint, default_sql, method)()
        print(output_string)
        return output_string

