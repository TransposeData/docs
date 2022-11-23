import secrets
import re

PYTHON_REQUEST_TEMPLATE_SQL = """import requests
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

CURL_REQUEST_TEMPLATE_SQL = """
curl --request POST \\
     --data {{'sql': '{}'}} \\
     --url '{}' \\
     --header 'accept: application/json' \\
     --header 'x-api-key: <YOUR API KEY>'
"""

JS_REQUEST_TEMPLATE_SQL = """
const fetch = require('node-fetch');
const url = '{}';
const sql_query = '{}';
const headers = {{
    'Content-Type': 'application
    }}
"""


class TransposeDocsInteractive:
    def _admonish(self, body: str, title="Give it a go!", type="example") -> str:
        return f'!!! {type} "{title}"\n' + self._indent(body)

    def _indent(self, string):
        return "\n".join(["    " + line for line in string.split("\n")])

    def _embed_into_switcher(self, switch_name, code):
        return f'=== "{switch_name}"\n' + self._indent(code)

    def _get_api_multilang(self):
        return "\n".join(
            [
                self._get_python(),
                #self._get_js(),
            ]
        )

    def _generate_code_fence(self, language, code):
        return '<code-fence switcher="false" lang="{}"><textarea vue-slot="code">{}</textarea></code-fence>'.format(
            language, code
        )


class APIKeyManager(TransposeDocsInteractive):
    def __init__(self):
        pass

    def __call__(self):
        return self._admonish('This page contains many interactive examples.  To run them, you\'ll need a Transpose API key.  To get this, [log in or sign up with Transpose](https://app.transpose.io).  Once you\'re logged in, navigate to your team dashboard.  Here, you can view and copy your keys.  Once you have your key, copy it into each example code snippet below.', title='API Key', type='warning')


        return self._admonish('\n'.join([
            'This page contains many interactive examples. To run them, you\'ll need a Transpose API key.  To get this, [log in or sign up with Transpose](https://app.transpose.io).  Once you\'re logged in, navigate to your team dashboard.  Here, you can view and copy your keys.  Once you have your key, copy it into the box below.',
            '<input type="text" id="api-key" placeholder="Your API Key" onChange="updateAPIKey(this.value)" style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;">',
            ]), title="API Key", type="warning")


class TransposeDocsSQL(TransposeDocsInteractive):
    def __init__(self, default_sql):
        super().__init__()
        self.endpoint = "https://api.transpose.io/sql"
        self.sql = default_sql
        self.unique_identifier = secrets.token_hex(8)

    def _preprocess_sql_for_string(self, sql):
        """
        Preprocesses the SQL query to make it more readable in the docs.
        """
        sql = sql.strip()
        sql = re.sub(r" *\/[*].*[*]\/ *\n", "", sql)
        return sql

    def _get_sql_entry(self):
        """
        Returns a Fenced Code Block with SQL syntax highlighting, where the body of the block is the SQL query.
        """
        return (
            "``` { .sql #"
            + self._get_sql_entry_id()
            + ' title="SQL Query" }\n'
            + f"{self.sql}\n"
            + "```"
        )

    def _get_sql_entry_id(self):
        return f"{self.unique_identifier}_sql_entry"

    def _get_python(self):
        code_snippet = PYTHON_REQUEST_TEMPLATE_SQL.format(self.endpoint, self.sql)
        return self._embed_into_switcher(
            "Python", self._generate_code_fence("py", code_snippet)
        )

    def _get_js(self):
        code_snippet = JS_REQUEST_TEMPLATE_SQL.format(self.endpoint, self.sql)
        return self._embed_into_switcher(
            "Node", self._generate_code_fence("js", code_snippet)
        )

    def __call__(self):
        return self._admonish(
            "\n".join([self._get_sql_entry(), self._get_api_multilang()])
        )

PYTHON_REQUEST_TEMPLATE_REST = """import requests
url = "{}"
headers = {{
    'Content-Type': 'application/json',
    'X-API-KEY': '<YOUR-API-KEY>',
}}
params = {}
response = requests.get(url, headers=headers, params=params)
print(response.text)
"""

class TransposeDocsRest(TransposeDocsInteractive):
    
    def __init__(self, endpoint, params):
        self.endpoint = endpoint
        self.params = params

    def _get_python(self):
        code_snippet = PYTHON_REQUEST_TEMPLATE_REST.format(self.endpoint, self.params)
        return self._embed_into_switcher(
            "Python", self._generate_code_fence("py", code_snippet)
        )


    def __call__(self):
        return self._admonish(
            "\n".join([self._get_api_multilang()])
        )


def define_env(env):

    @env.macro
    def get_transpose_api_key():
        output = APIKeyManager()()
        print(output)
        return output

    @env.macro
    def transpose_fenced_sql(default_sql: str) -> str:
        output = TransposeDocsSQL(default_sql)()
        print(output)
        return output

    @env.macro
    def transpose_fenced_rest(endpoint: str, params: dict) -> str:
        output = TransposeDocsRest(endpoint, params)()
        print(output)
        return output

