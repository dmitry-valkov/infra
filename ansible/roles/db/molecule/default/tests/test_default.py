# check if MongoDB is enabled and running
def test_mongo_running_and_enabled(host):
    mongo = host.service("mongod")
    assert mongo.is_running
    assert mongo.is_enabled
# check if configuration file contains the required line
def test_config_file(host):
    config_file = host.file('/etc/mongod.conf')
    assert config_file.contains('bindIp: 0.0.0.0')
    assert config_file.is_file

def test_db_port_file(host):
    config_file = host.file('/etc/mongod.conf')
    assert config_file.contains('port: 27017')
    assert config_file.is_file

def test_db_port_socket(host):
    socket = host.socket('tcp://0.0.0.0:27017');
    assert socket.is_listening;