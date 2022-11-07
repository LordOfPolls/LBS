import sys
import timeit

import yaml
from tabulate import tabulate

import samples

import hikari

bot = hikari.GatewayBot(token="token", banner=None, logs=None)
impl = hikari.impl.EntityFactoryImpl(bot)
impl.deserialize_message(payload=samples.message())


class LBS:
    def __init__(self, *, iterations: int = 500, debug: bool = False):
        with open("test_config.yml") as f:
            self.tests: dict = yaml.safe_load(f)
        with open("library_config.yml") as f:
            self.library_config: dict = yaml.safe_load(f)

        self.libs = sorted([l for l in self.library_config.keys()])
        self.padding = max(
            len(config["name"]) for config in self.library_config.values()
        )
        self.iterations = iterations
        self.debug = debug

    def _print_results(self, results: dict[str, float]) -> None:
        _results = {k: v * 1000000 for k, v in results.items()}

        fastest_library = min(_results, key=_results.get)

        out = [["Library", "Total Time(ms)", "Average Time(µs)", "Difference"]]
        for library, time in _results.items():
            diff_percent = (time - _results[fastest_library]) / _results[
                fastest_library
            ]
            out.append(
                [
                    f"{'🎉' if library == fastest_library else ''}{self.library_config[library]['name']}",
                    f"{time/1000:.2f}ms" if time != float("inf") else "DNF",
                    f"{time/self.iterations:.3f}µs" if time != float("inf") else "DNF",
                    f"{diff_percent:.2%}" if time != float("inf") else "DNF",
                ]
            )
        print(tabulate(out, headers="firstrow", tablefmt="github"))
        print()

    def _safe_test(
        self,
        code: str,
        number: int,
        library: str,
        setup: str | None = None,
        global_vars: dict[str, object] | None = None,
    ) -> float:
        try:
            return timeit.timeit(code, number=number, setup=setup, globals=global_vars)
        except Exception as e:
            if self.debug:
                print(f"Error in {library}: {e}")
            return float("inf")

    def _run_tests(self):
        for test in self.tests.values():
            results = {}
            print(
                f"{test['name']}:: {test['description'].format(iterations=self.iterations)}"
            )
            for library in self.libs:
                lib_config = self.library_config[library]
                if lib_config.get(test["code_key"]):
                    if test.get("req_cleanup", False):
                        setup = lib_config["cleanup"]
                    elif test.get("req_setup", False):
                        setup = lib_config.get("setup", "pass")
                    else:
                        setup = "pass"

                    time = self._safe_test(
                        lib_config[test["code_key"]],
                        number=self.iterations,
                        library=lib_config["name"],
                        setup=setup,
                        global_vars={"samples": samples},
                    )
                else:
                    time = float("inf")
                results[library] = time
            self._print_results(results)

    def run(self):
        print("LBS Pre-Alpha 0.0.0 -- LordOfPolls")
        print(f"Testing with python {sys.version}")
        print()
        print(f"Loaded {len(self.tests)} tests")
        print(f"Loaded {len(self.library_config)} libraries")
        print(", ".join([self.library_config[l]["name"] for l in self.libs]))
        self._run_tests()


tests = LBS()
tests.run()
