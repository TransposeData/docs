import secrets

PYTHON_REQUEST_TEMPLATE = """import requests
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
    }}
"""


class TransposeDocsInteractive:
    def _admonish(self, body: str, title="Give it a go!", type="example") -> str:
        return f'!!! {type} "{title}"\n' + self._indent(body)

    def _indent(self, string):
        return "\n".join(["    " + line for line in string.split("\n")])


class TransposeDocsSQL(TransposeDocsInteractive):
    def __init__(self, endpoint, sql, method):
        super().__init__()
        self.sql = sql
        self.endpoint = endpoint
        self.api_key = "<YOUR API KEY>"
        self.method = method
        self.unique_identifier = secrets.token_hex(8)

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

    def _get_python_code(self):
        """
        Returns a Fenced Code Block with Python syntax highlighting, where the body of the block is the Python code.
        """
        code_snippet = PYTHON_REQUEST_TEMPLATE.format(self.endpoint, self.sql)
        return ('=== "Python"\n' + "    ```py\n" + "{}\n" + "    ```").format(
            self._indent(code_snippet)
        )

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
        return ('=== "Curl"\n' + "    ```bash\n" + "{}\n" + "    ```").format(
            self._indent(code_snippet)
        )

    def _get_api_multilang(self):
        """
        Created tabbed view of various ways to call this API.
        """
        return "\n".join(
            [
                self._get_python_code(),
                self._get_node_code(),
                self._get_curl_code(),
            ]
        )

    def _get_sql_entry_id(self):
        return f"{self.unique_identifier}_sql_entry"

    def _get_query_output_id(self):
        return f"{self.unique_identifier}_query_output"

    def _get_run_query_button(self):
        request_to_issue = f"issueRequest(event, '{self._get_sql_entry_id()}', '{self._get_query_output_id()}')"
        return f'<a class="md_button run_query_button" onclick="{request_to_issue}">Run Query</a>'

    def _get_response_box(self):
        return (
            "```{ .json #"
            + self._get_query_output_id()
            + ' title="Response" }\n'
            + '{\n    "data": [],\n    "error": null,\n    "status": 200\n}\n```'
        )

    def _admonish(self, string):
        return '!!! example "Give it a go!"\n' + self._indent(string)

    def __call__(self):
        return self._admonish(
            "\n".join(
                [
                    self._get_sql_entry(),
                    self._get_api_multilang(),
                    self._get_run_query_button(),
                    self._get_response_box(),
                ]
            )
        )


class SQLCodeFence(TransposeDocsInteractive):
    def __init__(self, default_sql):
        super().__init__()
        self.endpoint = "https://api.transpose.io/sql"
        self.sql = default_sql
        self.unique_identifier = secrets.token_hex(8)

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

    def _generate_code_fence(self, language, code):
        return '<code-fence switcher="false" lang="{}"><textarea vue-slot="code">{}</textarea></code-fence>'.format(
            language, code
        )

    def _embed_into_switcher(self, switch_name, code):
        return f'=== "{switch_name}"\n' + self._indent(code)

    def _get_python(self):
        code_snippet = PYTHON_REQUEST_TEMPLATE.format(self.endpoint, self.sql)
        return self._embed_into_switcher(
            "Python", self._generate_code_fence("py", code_snippet)
        )

    def _get_js(self):
        code_snippet = JS_REQUEST_TEMPLATE.format(self.endpoint, self.sql)
        return self._embed_into_switcher(
            "Node", self._generate_code_fence("js", code_snippet)
        )

    def __call__(self):
        return self._admonish(
            "\n".join([self._get_sql_entry(), self._get_api_multilang()])
        )
        code = self._indent(PYTHON_REQUEST_TEMPLATE.format(self.endpoint, self.sql))
        return (
            f'=== "Python"\n'
            + f'    <code-fence switcher="false" lang="py"><textarea vue-slot="code">{code}</textarea></code-fence>\n'
            + f'=== "Node"\n'
            + f'    <code-fence switcher="false" lang="js"><textarea vue-slot="code">{code}</textarea></code-fence>\n'
            + f'=== "Curl"\n'
            + f'    <code-fence switcher="false" lang="bash"><textarea vue-slot="code">{code}</textarea></code-fence>\n'
        )


class TransposeDocsRest:
    pass


def define_env(env):
    @env.macro
    def transpose_fenced_sql(default_sql: str) -> str:
        output = SQLCodeFence(default_sql)()
        print(output)
        return output

    @env.macro
    def transpose_sql_endpoint(endpoint: str, default_sql: str, method: str):
        output_string = TransposeDocsSQL(endpoint, default_sql, method)()
        # print(output_string)
        return output_string
