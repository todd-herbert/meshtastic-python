"""Version lookup utilities, isolated for cleanliness"""
import sys
try:
    from importlib.metadata import version
except:
    import pkg_resources

def get_active_version():
    return "2.3.11"
