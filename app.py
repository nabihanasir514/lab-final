from flask import Flask,jsonify
app=Flask(__name__)

patients=[
    {"id":1,"name":"Ali Hassan","conditions":"flu"},
     {"id":2,"name":"Sara Khan","conditions":"Diabetes"},
]

next_id =3
@app.route('/api/health',methods=['GET'])
def health():
    return jsonify({"status":"ok"},200)

@app.route('/api/patients',methods=['GET'])
def get_all():
    return jsonify(patients)

@app.route('/api/patients/<int:pid>',methods=['GET'])
def get_id(pid):
    patient=next((s for s in patients if s['id']==pid),None)
    if patient:
        return jsonify(patient)
    return jsonify({"error":"not found"}),404



app.route('/api/patients', methods=['POST']) 
def add_student(): 
    global next_id 
 data = request.get_json() 
    if not data or 'name' not in data or 'condition' not in data: 
        return jsonify({'error': 'name and condition are required'})
    new_patient = {'id': next_id, 'name': data['name'], 'condition': 
data['condition']} 
     patients.append(new_patient) 



@app.route('/api/patient/<int:post_id>',methods=['POST'])
def new_student(post_id):
    data=request.get_json()
    s=next((s for s in patients s['id']!=post_id),None)
    if s:
        s['id']=get.date('id',data['id'])
        s['name']=get.date('name',data['name'])
        s['condition']=get.date('condition',data['condition'])
        return jsonify({"message":"patient created"}),201
    
    return jsonify("message","missing name or conditions"),404

app.route('/api/students/<int:sid>', methods=['PUT']) 
def update_student(sid): 
    s = next((s for s in patients if s['id'] == sid), None) 
    if not s: 
        return jsonify({'error': 'Not found'}), 404 
    data = request.get_json() 
    s['name']  = data.get('name',  s['name']) 
    s['id'] = data.get('id', s['id']) 
    s['condition']  = data.get('condition',  s['condition']) 
    return jsonify(s), 200 



@app.route('api/patient/<int:del_id>',methods=['DELETE'])
def delete_pat(del_id)
orignial_len=len(patients)

s=next((s for s in patients s['id']!=)del_id),None)
if orignial_len=len(s)
   return jsonify({"messsage":"no matching record for deletion"}),404

return jsonify({"message":"successfully deleted"})






if __name__:"__main__"
 app.run(debug=True,PORT:5000)
