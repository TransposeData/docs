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
        return ('```sql title="SQL Query"\n' +
                '{}\n' +
                '```').format(self.sql)

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

    def _get_run_query_button(self):
        sql_to_inject = self.sql.replace('"', "'").replace("'", "&quot;").replace('\n', ' ')
        print(sql_to_inject)
        request_to_issue = f'issueRequest(event, \'{sql_to_inject}\')'
        print(request_to_issue)
        return f'<a class="md_button run_query_button" onclick="{request_to_issue}">Run Query</a>'


        return "<a class=\"md_button run_query_button\" onclick=\"issueRequest(event, \'{}\' ) \" >Run Query</a>".format(self.sql.replace('\n', ''))

    def _get_response_box(self):
        return '```json title="Response"\n{\n    "data": [],\n    "error": null,\n    "status": 200\n}\n```'

    def _indent(self, string):
        return '\n'.join(['    ' + line for line in string.split('\n')])

    def _admonish(self, string):
        return '!!! example "Give it a go!"\n{}'.format(self._indent(string))

    def __call__(self):
        return self._admonish('\n'.join([
            self._get_sql_entry(),
            self._get_api_multilang(),
            self._get_run_query_button(),
            self._get_response_box(),
        ]))

def define_env(env):

    @env.macro
    def transpose_sql_endpoint(endpoint: str, default_sql: str, method: str):
        output_string = TransposeDocsSQL(endpoint, default_sql, method)()
        print(output_string)
        print('reeeeee')
        return output_string

