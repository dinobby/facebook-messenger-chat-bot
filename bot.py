import os, sys
import requests
from flask import Flask, request, send_from_directory
#from bottle import route, run, request, abort, static_file
from fsm import TocMachine

'''
I'm using Flask for the main framework,
and bottle for the finite state machine graph.
'''

app = Flask(__name__)

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'state1_going_to_state2'
        },
		{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state3',
            'conditions': 'state1_going_to_state3'
        },
		{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state4',
            'conditions': 'state1_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'state2_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state5',
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state1',
            'conditions': 'state5_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state6',
            'conditions': 'state3_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state6',
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state1',
            'conditions': 'state6_going_to_state1'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state2',
                'state3',
                'state4',
                'state5',
                'state6'
            ],
            'dest': 'state1'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

@app.route('/', methods=['GET'])
def verify():
    '''
    verify webhook subscription, for the verification code being 'hello'.
    '''
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "verified", 200

@app.route('/', methods=['POST'])
def webhook():
    '''
    this function handles webhook events.
    '''
    print('\nFSM STATE: ' + machine.state)
    data = request.get_json()
    log(data)
    
    if data['object'] == "page":
        event = data['entry'][0]['messaging'][0]
        if 'message' in event:
            if event['message']['text'] == '返回' and machine.state == 'state5':
                machine.go_back(event)
            elif  event['message']['text'] == '返回' and machine.state == 'state6':
                machine.go_back(event)
            elif event['message']['text'] and machine.state == 'state4':
                machine.go_back(event)
            else:
                machine.advance(event)
        
    return "ok", 200

# @route('/show-fsm', methods=['GET'])
# '''this function is for drawing.'''
# def show_fsm():
#     machine.get_graph().draw('fsm.png', prog='dot', format='png')
#     return static_file('fsm.png', root='./', mimetype='image/png')

def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    #run(host="localhost", port=5001, debug=True)