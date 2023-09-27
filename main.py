from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/is-new/<plugin>")
def is_new(plugin):
    instance = request.args.get("instance")
    file = open('./'+instance+'/user-plugins.yaml', 'r')
    plugins=[]
    for each in file:
        if 'id' in each:
            each=each.replace("- id: ","")
            each=each.strip()
            plugins.append(each)
    plugin=plugin.strip()
    if plugin not in plugins:
        return "true"
    return "false"
if __name__ == "__main__":
    app.run(debug=True)