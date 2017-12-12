def percentage(part, whole):
    """
    Compute percentage.
    :param part: Part.
    :param whole: Whole.
    :return: Percentage.
    """
    return 100 * float(part) / float(whole)


def df_to_latex(path, df):
    """
    Persists pandas dataframe as .text table.
    :param path: Path to .tex file to write to.
    :param df: Dataframe to persist.
    :return:
    """
    with open(path, 'w') as f:
        f.write(df.to_latex(index=False))
