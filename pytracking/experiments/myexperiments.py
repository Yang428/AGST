from pytracking.evaluation import Tracker, get_dataset, trackerlist


def got10k():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('got10k_test')
    return trackers, dataset


def otb():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('otb')
    return trackers, dataset

def trackingnet():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('trackingnet')
    return trackers, dataset

def uav():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('uav')
    return trackers, dataset

def lasot():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('lasot')
    return trackers, dataset

def tpl():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('tpl')
    return trackers, dataset

def nfs():
    trackers = trackerlist('agst', 'agst', range(1))

    dataset = get_dataset('nfs')
    return trackers, dataset
