from robot.libraries.BuiltIn import BuiltIn


def open_to_application_url(host, endpoint=None):
    """
    Generate the url for the application dynamically
    :params protocol: https/http
    :params domain: app_name
    :params host: app_host
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    if endpoint is None:
        endpoint = ""
    # if domain:
    #   return se2lib.go_to(f'https://{domain}-{host}.com/{endpoint}')
    return se2lib.go_to(f'https://{host}.com/{endpoint}')
