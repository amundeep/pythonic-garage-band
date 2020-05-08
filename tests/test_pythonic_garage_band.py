from pythonic_garage_band import __version__
from abc import ABC, abstractmethod
from pythonic_garage_band.garage_band import Band, Guitarist, Singer, Drummer
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_guitarist():
    john = Guitarist("John Mayer")
    assert john.name == "John Mayer"
    assert john.instrument == "Guitar"
    assert john.play_solo() == "DI DI DOO DA"

def test_get_instrument():
    travis = Drummer("Travis Barker")
    assert travis.get_instrument() == "Drumset"

def test_musician_repr():
    slash = Guitarist("Slash")
    assert slash.__repr__() == "{'name': Slash, 'instrument': Guitar}"

def test_musician_str():
    slash = Guitarist("Slash")
    assert slash.__str__() == "Musician(Slash, Guitar)" 

def test_band_to_list():
    band1 = Band("One Man Yes Band", [Guitarist("Jim Carey")])
    band2 = Band("Obi-Wan Kenoband", [Drummer("Anakin")])
    assert len(Band.to_list()) == 2

def test_band_name(coldplay):
    assert coldplay.name == "Coldplay"

def test_play_solos(coldplay):
    assert coldplay.play_solos() == "DI DI DOO DA LET IT GO BADDUM TSS"

# def test_band_repr(coldplay):
#     assert coldplay.members == ""

@pytest.fixture
# set up fixed object in pytest
def coldplay():
    coldplay = Band("Coldplay", [
        Guitarist("Guy Berryman"),
        Singer("Chris Martin"),
        Drummer("Will Champion"),
    ])

    return coldplay

