import secrets
import re

PYTHON_REQUEST_TEMPLATE_SQL = """import requests
url = "{}"
sql_query = \"\"\"{}\"\"\"
headers = {{
    'Content-Type': 'application/json',
    'X-API-KEY': 'FxKTp6MHpWQDaos8SRnSetdIZiUYLliS',
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

    def _generate_code_fence(self, language, code):
        return '<code-fence class="transpose_demo" switcher="false" lang="{}" cache="false"><textarea vue-slot="code">{}</textarea></code-fence>'.format(
            language, code
        )


class APIKeyManager(TransposeDocsInteractive):
    def __init__(self):
        pass

    def __call__(self):
        return self._admonish(
            """Before proceeding, we need to authenticate ourselves with Transpose.  To access any Transpose API, you'll need an API key.  All API requests should include your API key in an `X-API-KEY` header.  If you haven't already, you'll need to [sign up and create a team (for free!)](https://app.transpose.io).  Once you have a team, you can find a list of your API keys in your team dashboard.  When you have your API key, replace `<YOUR-API-KEY>` in the interactive examples below with your key.

Remember not to share your API key!  Your API key is a secret, and should not be stored or exposed in a public manner.""",
            title="API Key",
            type="warning",
        )


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
        sql = re.sub(r"\*", "\*", sql)
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

    def _get_api_multilang(self):
        return "\n".join(
            [
                self._get_python(),
                self._get_js(),
            ]
        )

    def _get_python(self):
        code_snippet = PYTHON_REQUEST_TEMPLATE_SQL.format(self.endpoint, self._preprocess_sql_for_string(self.sql))
        return self._embed_into_switcher(
            "Python", self._generate_code_fence("py", code_snippet)
        )

    def _get_js(self):
        code_snippet = JS_REQUEST_TEMPLATE_SQL.format(self.endpoint, self._preprocess_sql_for_string(self.sql))
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
    'X-API-KEY': 'FxKTp6MHpWQDaos8SRnSetdIZiUYLliS',
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

    def _get_api_multilang(self):
        return "\n".join(
            [
                self._get_python(),
                # self._get_js(),
            ]
        )


    def __call__(self):
        return self._admonish("\n".join([self._get_api_multilang()]))

class TransposeDocsColoredLink:
    def __init__(self, url, color, text, description):
        self.url = url
        self.color = color
        self.text = text
        self.description = description

    def get_color_gradient(self) -> str:
        color_map = {
                "purple": "linear-gradient(to bottom right, blue, purple)",
                "red": "linear-gradient(to bottom right, red, orange)",
                "blue": "linear-gradient(to bottom right, blue, cyan)",
                "green": "linear-gradient(to bottom right, green, lime)",
        }

        return color_map[self.color]


    def __call__(self):
        return """
<a markdown="1" class="colored-link" href="https://www.google.com">
<div markdown="1" class="colored-square" style="background-image: {};">
<div markdown="1">

:material-fast-forward:

</div>
</div>


<div class="text-container">
<p class="text">{}</p>
<p class="description">{}</p>
</div>
</a>
""".format(self.get_color_gradient(), self.text, self.description)


def define_env(env):
    @env.macro
    def get_transpose_api_key():
        output = APIKeyManager()()
        return output

    @env.macro
    def transpose_fenced_sql(default_sql: str) -> str:
        output = TransposeDocsSQL(default_sql)()
        return output

    @env.macro
    def transpose_fenced_rest(endpoint: str, params: dict) -> str:
        output = TransposeDocsRest(endpoint, params)()
        return output

    @env.macro
    def transpose_colored_link(url: str, color: str, text: str, description: str) -> str:
        output = TransposeDocsColoredLink(url, color, text, description)()
        print(output)
        return output
