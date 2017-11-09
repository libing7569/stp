service ServerCommunicate{
    string ping(),
	string notify(1:string ip, 2:i64 port),
    string sync_tasks(1: map<string,string> tasksList),
	string get_task(1:string taskid),
	string update_task(1:string taskid),
	string get_server_stat()
}
