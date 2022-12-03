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
        'sql': sql_query,{}
    }},
)
print(response.text)
print('Credits charged:', response.headers.get('X-Credits-Charged', None))
"""

CURL_REQUEST_TEMPLATE_SQL = """
curl --request POST \\
     --data {{'sql': '{}'}} \\
     --url '{}' \\
     --header 'accept: application/json' \\
     --header 'x-api-key: <YOUR API KEY>'
"""

JS_REQUEST_TEMPLATE_SQL = """
const options = {
  method: 'POST',
  headers: {accept: 'application/json', 'x-api-key': 'FxKTp6MHpWQDaos8SRnSetdIZiUYLliS'},
  body: JSON.stringify({sql: '{}'})
};
fetch('{}', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
"""

JS_REQUEST_TEMPLATE_SQL1 = """
const fetch = require('node-fetch');
const url = '{}';
const sql_query = '{}';
const headers = {{
    'Content-Type': 'application
}}
"""


class TransposeDocsInteractive:
    def _admonish(self, body: str, title="Give it a go!", type="example") -> str:
        if type == 'warning':
            return f'!!! {type} "{title}"\n' + self._indent(body)
        return body

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
    def __init__(self, default_sql, options: dict=None):
        super().__init__()
        self.endpoint = "https://api.transpose.io/sql"
        self.sql = default_sql
        self.unique_identifier = secrets.token_hex(8)
        self.options = options

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
                #self._get_js(),
            ]
        )

    def _get_python(self):
        code_snippet = PYTHON_REQUEST_TEMPLATE_SQL.format(self.endpoint, self._preprocess_sql_for_string(self.sql), self._get_python_options())
        return self._embed_into_switcher(
            "Python", self._generate_code_fence("py", code_snippet)
        )

    def _get_python_options(self):
        if self.options is None:
            return ""
        return '\n\t\t\'options\': {\n\t\t\t' + ",\n\t\t\t".join([f"'{key}': {value}" for key, value in self.options.items()]) + "\n\t\t}"

    def _get_js(self):
        code_snippet = JS_REQUEST_TEMPLATE_SQL.format(self._preprocess_sql_for_string(self.sql), self.endpoint)
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
    def __init__(self, link_type, url, text, description, custom_color=None, custom_icon=None):
        self.link_type = link_type
        self.url = self.get_url_from_link_type() if url is None else url
        self.text = self.get_text_from_link_type() if text is None else text
        self.description = self.get_description_from_link_type() if description is None else description

        self.icon = self.get_icon_from_link_type() if custom_icon is None else custom_icon
        self.color = self.get_color_from_link_type() if custom_color is None else custom_color

    def get_url_from_link_type(self):
        url_map = {
            'discord': 'https://discord.gg/transpose',
            'rest': '/rest/overview',
            'sql': '/sql/overview',
            'quickstart': '/quickstart',
            'block': '/rest/block-api/overview',
            'nft': '/rest/nft-api/overview',
            'token': '/rest/token-api/overview',
            'ens': '/rest/ens-api/overview',
            'playground': 'https://playground.transpose.io',
            'atlas': 'https://playground.transpose.io',
        }
        return url_map[self.link_type]

    def get_description_from_link_type(self):
        desc_map = {
            'discord': 'Discord is the primary home of the Transpose developer community.  Join us to ask questions, share your work, and get help.',
            'rest': 'Explore highly optimized queries for key blockchain primitives.',
            'sql': 'Start writing instantaneous, powerful and hyper-flexible queries against arbitrary real-time blockchain data.',
            'quickstart': 'Get started with both our REST and SQL APIs in less than 5 minutes.',
            'block': 'Retrieve accounts, blocks, transactions, and logs in bulk.',
            'nft': 'Query any collection, NFT, owner, mint, transfer, burn, or sale.',
            'token': 'Lookup any token, transfer, balance, DEX swap, liquidity event, and more.',
            'ens': 'Search for and resolve any ENS record using name, account, expiration, and more.',
            'playground': 'Write and execute SQL queries in our browser-based development tool.',
            'atlas': 'Explore and contribute to queries created by the Transpose community.',
        }
        return desc_map[self.link_type]

    def get_text_from_link_type(self):
        text_map = {
            'discord': 'Join our Discord',
            'rest': 'Explore our REST API Documentation',
            'sql': 'Explore our SQL API Documentation',
            'quickstart': 'Visit our Quickstart Guide',
            'block': 'Block API',
            'nft': 'NFT API',
            'token': 'Token API',
            'ens': 'ENS API',
            'playground': 'Explore the Playground',
            'atlas': 'Explore the Atlas',
        }
        return text_map[self.link_type]

    def get_color_from_link_type(self):
        color_map = {
            "discord": 'purple',
            "block": 'blue',
            "nft": 'green',
            "token": 'yellow',
            "ens": 'orange',
            "rest": 'blue',
            "sql": 'green',
            "quickstart": 'orange',
            "playground": 'blue',
            "atlas": 'orange',
        }
        if self.link_type in color_map:
            return color_map[self.link_type]
        else:
            return 'orange'

    def get_color_gradient(self) -> str:
        gradient_map_hex = {
                'purple': 'linear-gradient(to bottom right, #0000ff, #A020F0)',
                'orange': 'linear-gradient(to bottom right, #FF4500, #FFA500)',
                'blue': 'linear-gradient(to bottom right, #0000ff, #00BFFF)',
                'green': 'linear-gradient(to bottom right, #008000, #00FF00)',
                'yellow': 'linear-gradient(to bottom right, #FFD700, #EEEE00)',
        }

        return gradient_map_hex[self.color]

    def get_icon_from_link_type(self) -> str:
        icon_map = {
            "ens": 'material-triangle-outline',
            "block": 'material-square-outline',
            "token": 'material-hexagon-outline',
            "nft": 'material-star-outline',
            "discord": "simple-discord",
            "quickstart": 'material-rocket-launch',
            "sql": 'material-database',
            "rest": 'material-cloud-braces',
            "atlas": 'material-map-outline',
            "playground": 'material-laptop',
        }

        return icon_map[self.link_type]

    def __call__(self):
        return """
<a markdown="1" class="colored-link" href="{}">
<div markdown="1" class="colored-link-container">
<div markdown="1" class="colored-square" style="background-image: {};">
<div markdown="1">

:{}:

</div>
</div>
</div>


<div class="text-container">
<p class="text">{}</p>
<p class="description">{}</p>
</div>
</a>
""".format(self.url, self.get_color_gradient(), self.icon, self.text, self.description)


class TransposeDocsCodeInteractive(TransposeDocsInteractive):
    def __init__(self, code, language):
        self.code = code
        self.language = language

    def __call__(self):
        return self._generate_code_fence(self.language, self.code)

def define_env(env):
    @env.macro
    def get_transpose_api_key():
        output = APIKeyManager()()
        return output

    @env.macro
    def transpose_fenced_sql(default_sql: str, options: dict=None) -> str:
        output = TransposeDocsSQL(default_sql, options)()
        return output

    @env.macro
    def transpose_fenced_rest(endpoint: str, params: dict) -> str:
        output = TransposeDocsRest(endpoint, params)()
        return output

    @env.macro
    def transpose_colored_link(link_type, url=None, text=None, description=None, custom_color=None, custom_icon=None) -> str:
        output = TransposeDocsColoredLink(link_type, url, text, description, custom_color, custom_icon)()
        return output

    @env.macro
    def transpose_fenced_code_interactive(code: str, language: str) -> str:
        output = TransposeDocsCodeInteractive(code, language)()
        print(output)
        return output
