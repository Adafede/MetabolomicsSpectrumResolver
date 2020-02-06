import sys
sys.path.insert(0, "..")
import parsing  # noqa: E402
from usi_test_cases import test_usi_list


def test_uri_parse():
    for usi in test_usi_list:
        parsing.parse_usi(usi)  

def test_render_mirror():
    import views

    plotting_params = views.default_plotting_args
    plotting_params["mz_min"] = 0
    plotting_params["mz_max"] = 250
    views._generate_mirror_figure('mzdata:MASSBANK:BSU00002', 'mzdata:MASSBANK:BSU00002', "png", **plotting_params)