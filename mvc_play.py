# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects:
            item_template = self.template
            for field in self.model.fields:
                if item.has_key(field):
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output


# CONTROLLER: Routes messages
class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()

# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score"])
app.models["game"] = Model("game", ["game_name", "description"])


# load model objects form database tables
#app.models["user"].objects = [
#     {"name": "Bob", "score": "9"},
#     {"name": "Carol", "score": "11"},
#     {"name": "Ted", "score": "15"},
#     {"name": "Alice", "score": "13"}
# ]

app.models["game"].objects = [
    {"game_name": "Tetris", "description": "Shapes that fall"},
    {"game_name": "Frogger", "description": "Frogs that jump"},
    {"game_name": "Asteroids", "description": "Shoot the ships"},
    {"game_name": "Pong", "description": "Bounce the ball"}
]

#modelViewTemplate = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
modelViewTemplate = "\nThe game is <em>{{game_name}}</em>, the description is<strong>{{description}}</strong>.<br>\n"

#scoresView = View(modelViewTemplate, app.models["user"])
descrView = View(modelViewTemplate, app.models["game"])

# #app.controller.routes = {
#     "/scores/": scoresView
# }

app.controller.routes = {
    "/avail_games/": descrView
}

request_path = "/avail_games/"
response_html = app.controller.route(request_path)
print response_html
