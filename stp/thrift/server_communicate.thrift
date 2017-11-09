service ServerCommunicate{
    string ping(),
	string notify(1:string ip, 2:i64 port),
	string get_task(1:string taskid),
	string get_server_stat()
}
