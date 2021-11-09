def employee(**info):
    print(info)


employee(name="John", age=30, salary=25000)

print("\n")


def to_do(**to_do_status):
    return to_do_status


to_do_status_result = to_do(
    get_coffe="Done",
    exercise="In Progress",
    watch_tv="Not Started"
)

print(to_do_status_result)
