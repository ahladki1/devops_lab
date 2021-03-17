import requests

token = {'Authorization': 'token'}


def get_pulls(state):
    return get_pulls_get(state)[1]


def get_pulls_get(state):
    resp = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
    resp_search = 'https://api.github.com/search/issues?q=is:pr%20label:'
    item = requests.get(resp, headers=token)

    if state in ['open', 'closed']:
        item = requests.get(resp,
                            headers=token,
                            params={'state': '{0}'.format(state),
                                    'per_page': '100'})
        return item.status_code, get_inform(state, item.json())
    elif state in ['accepted', 'needs work']:
        item = requests.get(resp_search + f'\"{state}\"\
                   %20repo:alenaPy/devops_lab&per_page=100',
                            headers=token,
                            params={'per_page': '100'})
        return item.status_code, get_inform(state, item.json())
    else:

        return item.status_code, get_inform(state, item.json())


def get_inform(state, it):
    if state in ['open', 'closed']:
        return it
    if state in ['accepted', 'needs work']:
        return it['items']
    return it
