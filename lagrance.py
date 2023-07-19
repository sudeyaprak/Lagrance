def lagrange(eph, dat):
    """
    Interpolates the variable value at epoch `eph` using Lagrange interpolation.
    
    Args:
        eph (float): Interpolation epoch.
        dat (ndarray): 10x2 matrix (or corresponding vector) with time tags (t) in the 1st column
                       and variable values at grid points in the 2nd column.
        
    Returns:
        float: Interpolated value for the variable at epoch `eph`.
    """
    
    t = eph
    t_grid = dat[:, 0]
    n = len(t_grid)
    result = 0
    
    # Iterate over each grid point
    for i in range(n):
        div_res = 1
        
        # Calculate the Lagrange interpolation polynomial
        for j in range(n):
            if i == j:
                continue
            else:
                dif = (t - t_grid[j]) / (t_grid[i] - t_grid[j])
                div_res *= dif
                
        # Evaluate the polynomial at epoch `eph` and add to the result
        result += dat[i, 1] * div_res
        
    return result
