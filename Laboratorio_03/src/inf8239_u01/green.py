def pareto_flags(
    df,
    score="f1_macro",
    cost="fit_median_s"
):
    flags = []

    for _, row in df.iterrows():

        dominated = (
            (
                (df[score] >= row[score])
                &
                (df[cost] <= row[cost])
                &
                (
                    (df[score] > row[score])
                    |
                    (df[cost] < row[cost])
                )
            )
        ).any()

        flags.append(
            not bool(dominated)
        )

    return flags