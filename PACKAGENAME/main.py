class PACKAGENAME:
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        """An AnnData object with a GRN matrix in varp["GRN"]

        Args:
            grn: scipy.sparse.csr_matrix | np.ndarray a matrix with zeros and non-zeros
                signifying the presence of an edge and the direction of the edge
                respectively. The matrix should be square and the rows and columns
                should correspond to the genes in the AnnData object.
                The row index correpond to genes that are regulators and the column
                index corresponds to genes that are targets.

        @see https://anndata.readthedocs.io for more informaiotn on AnnData objects
        """
