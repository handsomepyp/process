# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pm4py


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(h)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    bpmn_graph = pm4py.read_bpmn("dataset/ex00_writer0001.bpmn")
    # print(bpmn_graph)
    from pm4py.objects.conversion.bpmn import converter as bpmn_converter

    net, im, fm = bpmn_converter.apply(bpmn_graph)
    print(net)
    print(im)
    print(fm)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
