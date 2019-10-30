def get_driver(driver_name, resultSet):
    for result in resultSet:
        if driver_name == result.driver.person_name:
            return result.driver
    return None
