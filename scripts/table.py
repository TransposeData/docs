import yaml
import os

def output(v: dict, root: str):
    meta = v['meta']
    schema = v['schema']
    exists = os.path.exists('{}'.format(root))
    if not exists:
        os.makedirs('{}'.format(root))
    fn = '{}/{}.md'.format(root, meta['table'])
    print('- \'{}\''.format(fn))
    with open(fn, 'w') as file:
        file.write('# {}\n\n'.format(k))
        file.write('{}\n\n'.format(meta['description']))
        file.write('| Name                | Description                                                                 | Type        |\n')
        file.write('| --------- | --------- | --------------------------------------------------------------------------- |\n')
        for column in schema:
            file.write('| {} | {} | `{}` |\n'.format(column['column'], column['description'], column['type']))

with open('ethereum.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)

    for layer,tables in prime_service.items():
        for table in tables:
            for k,v in table.items():
                if isinstance(v, dict):
                    meta = v['meta']
                    schema = v['schema']
                    exists = os.path.exists('docs/SQL/tables/{}'.format(layer))
                    if not exists:
                        os.makedirs('docs/SQL/tables/{}'.format(layer))
                    fn = 'docs/SQL/tables/{}/{}.md'.format(layer, meta['table'])
                    print('- \'{}\''.format(fn))
                    with open(fn, 'w') as file:
                        file.write('# {}\n\n'.format(k))
                        file.write('{}\n\n'.format(meta['description']))
                        file.write('| Name                | Description                                                                 | Type        |\n')
                        file.write('| --------- | --------- | --------------------------------------------------------------------------- |\n')
                        for column in schema:
                            file.write('| {} | {} | `{}` |\n'.format(column['column'], column['description'], column['type']))
                else:
                    for table in v:
                        for k,v in table.items():
                            if isinstance(v, dict):
                                output(v, 'docs/SQL/tables/{}/{}'.format(layer, k))

                

