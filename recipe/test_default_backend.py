import h5netcdf

with h5netcdf.File("test.nc", "w") as f:
    f.create_variable("x", data=1.0)

with h5netcdf.File("test.nc", "r") as f:
    assert f["x"][()] == 1.0
