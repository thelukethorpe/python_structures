from filthyrat.structures import DummyStructure


def test_dummy_structure_add_and_len() -> None:
    ds = DummyStructure()
    ds.add(10)
    ds.add(20)

    assert len(ds) == 2
