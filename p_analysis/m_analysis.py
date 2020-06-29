

# Function to group by the columns below defined and count by all the unique id's (Quantity column defined in the
# acquisition module). The function also calculates the Percentage column.
def analyze(rural):
    group_rural = rural.groupby(['Country', 'Job_name', 'Rural'], as_index=False).count()
    group_rural['Percentage'] = group_rural['Quantity'].apply(
        lambda qtty: str((qtty * 100 / group_rural['Quantity'].sum()).round(2)) + '%')
    return group_rural
