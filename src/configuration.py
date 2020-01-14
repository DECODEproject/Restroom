from middleware import Middleware


class DebugMiddleware(Middleware):
    def _input_run(self):
        print("INPUT" * 200)

    def _output_run(self):
        print("OUTPUT" * 200)

    def get_name(self):
        return 'debug'

    def output(self):
        self._output_run()

    def input(self):
        self._input_run()


class LogMiddleware(Middleware):
    def _input_run(self):
        print("LOGIN" * 200)

    def _output_run(self):
        print("LOGOUT" * 200)

    def get_name(self):
        return 'log'

    def output(self):
        self._output_run()

    def input(self):
        self._input_run()


class Configuration:
    def __init__(self):
        self.middlewares = {}

    def register_middleware(self, middleware):
        if not isinstance(middleware, Middleware):
            raise RuntimeError('The middleware is not a good one')
        self.middlewares.setdefault(middleware.get_name(), middleware)

    def input(self):
        for m in self.middlewares.values():
            m.input()

    def output(self):
        for m in self.middlewares.values():
            m.output()

    @property
    def registered_middleware(self):
        return self.middlewares.keys()


configuration = Configuration()
configuration.register_middleware(DebugMiddleware())
configuration.register_middleware(LogMiddleware())
