import polars as pl

df = pl.read_csv("master.csv")
df = df.select("name", "mean")
df = df.filter(pl.col("name").str.contains("comp"))
df = df.with_columns(pl.col("name").str.strip_prefix("tests/test_benchmarks.py::test_").alias("name"))
dfMaster = df.rename({"mean":"mean_master"})

df = pl.read_csv("merged.csv")
df = df.select("name", "mean")
df = df.filter(pl.col("name").str.contains("comp"))
df = df.with_columns(pl.col("name").str.strip_prefix("tests/test_benchmarks.py::test_").alias("name"))
dfMerged = df.rename({"mean":"mean_merged"})

df = dfMerged.join(on="name", other=dfMaster)
df = df.with_columns((pl.col("mean_merged")-pl.col("mean_master")).alias("delta"))
df = df.with_columns((100*((pl.col("mean_merged")-pl.col("mean_master"))/pl.col("mean_master"))).alias("%"))
df.write_excel("speed_comparison.xlsx")


