from ktnas.read_data import read_microwave1


def test_reading_microwave1_data():

    df = read_microwave1()

    assert df.iat[0, 0] == 2074513
