import secrets

class TransposeDocsSQL:

    def __init__(self, endpoint, sql, method):
        self.sql = sql
        self.endpoint = endpoint
        self.api_key = '<YOUR API KEY>'
        self.method = method
        self.unique_identifier = secrets.token_hex(8)


    def _get_sql_entry(self):
        return '```sql\n{}\n```'.format(self.sql)

    def _get_python_code(self):
        return '=== "Python"\n\t```py\n\tprint(test)\n\t```'

    def _get_node_code(self):
        return '=== "Node"\n\t```js\n\tconsole.log("Hello World")\n\t```'

    def _get_api_multilang(self):
        return '\n'.join([
            self._get_python_code(),
            self._get_node_code(),
        ])

    def _get_run_query_button(self):
        return '<a class="md_button md_typeset" onclick="{}">Run Query</a>'.format(self._get_fetch_request())

    def _get_fetch_request(self):
        return "console.log('Hello World');"
 
    def _indent(self, string):
        return '\n'.join(['    ' + line for line in string.split('\n')])

    def _admonish(self, string):
        return '!!! example "Give it a go!"\n{}'.format(self._indent(string))

    def __call__(self):

        return self._admonish('\n'.join([
            '### SQL:',
            self._get_sql_entry(),
            '### API:',
            self._get_api_multilang(),
            self._get_run_query_button(),
        ]))

def define_env(env):
    "Hook function"

    @env.macro
    def transpose_sql_endpoint(endpoint: str, default_sql: str, method: str):
        output_string = TransposeDocsSQL(endpoint, default_sql, method)()
        print(output_string)
        print('reeeeee')
        return output_string

    @env.filter
    def my_filter(value):
        "Filter function"
        return value.upper()
