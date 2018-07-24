Mode <- function(x) {
     ux <- unique(x)
     ux[which.max(tabulate(match(x, ux)))]
}

Mode <- function(x) {
    if (is.numeric(x)) {
        x_table <- table(x)
        return(as.numeric(names(x_table)[which.max(x_table)]))
    }
}
