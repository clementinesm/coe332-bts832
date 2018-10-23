from hw1.hw1 import f,g,h

# First we test the f function
def test_f_list_return():
    assert type(f()) == list

def test_f_dict_elements():
    assert type(f()[0]) == dict

def test_f_three_keys():
    assert len(f()[0]) == 3

def test_f_value_type():
    assert type(f()[0]['id']) == int
    assert type(f()[1]['rain']) == float

def test_f_num_dicts():
    assert len(f()) == 4

def test_f_first_and_last():
    assert (f()[0]) == {'id':1,'year':1980,'rain':32}
    assert (f()[-1]) == {'id':4,'year':1983,'rain':36.7}


# Now test the g function
def test_g_list_return():
    assert type(g()) == list

def test_g_dict_elements():
    assert type(g()[0]) == dict

def test_g_three_keys():
    assert len(g()[0]) == 3

def test_g_value_type():
    assert type(g()[0]['id']) == int
    assert type(g()[1]['rain']) == float

def test_g_all_return():
    assert len(g()) == len(f())

def test_g_start():
    assert g(start = f()[0]['year'])[0]['year'] == f()[0]['year']

def test_g_end():
    assert g(end = f()[0]['year'])[0]['year'] == f()[0]['year']

def test_g_start_and_end():
    assert g(start = f()[0]['year'],end = f()[-1]['year'])[0]['year'] == f()[0]['year']
    assert g(start = f()[0]['year'],end = f()[-1]['year'])[-1]['year'] == f()[-1]['year']

def test_g_start_end_combo():
    assert len(g(start = f()[-1]['year'] + 1,end = f()[-1]['year'])) == 0


# Lastly test the h function
def test_h_list_return():
    assert type(h()) == list

def test_h_dict_elements():
    assert type(h()[0]) == dict

def test_h_three_keys():
    assert len(h()[0]) == 3

def test_h_value_type():
    assert type(h()[0]['id']) == int
    assert type(h()[1]['rain']) == float

def test_h_all_return():
    assert len(h()) == len(f())

def test_h_limit():
    assert len(h(limit = 1)) == 1

def test_h_offset():
    assert h(offset = 1)[0]['id'] == 2
    assert h(offset = 2)[0]['id'] == 3

def test_h_limit_and_offset():
    assert h(limit = 2,offset = 2)[0]['id'] == 3
    assert h(limit = 2,offset = 2)[-1]['id'] == 4

def test_h_limit_offset_combo():
    assert len(h(limit = len(f()) + 1)) == len(f())
    assert len(h(offset = len(f()) + 1)) == 0
