import numpy as np

def single_triangular_signal(amplitude, time):
    n = len(time)
    signal_array = np.zeros_like(time)
    signal_array[n//4:n//2] = amplitude*((2*time[n//4:n//2]/np.pi)+1)
    signal_array[n//2:3*n//4] = amplitude*((-2*time[n//2:3*n//4]/np.pi)+1)
    return signal_array

def time_array(start, finish, number_of_points):
    return np.linspace(start, finish, number_of_points)

def square_signal(amplitude, time,number_of_squares):
    time_array_length = len(time)
    signal_array = np.zeros_like(time)
    step = int(time_array_length/number_of_squares)
    start =0
    for interval_rank in range(number_of_squares):
        if interval_rank % 2 == 0:
            signal_array[start:start+step] = amplitude
        start += step
    return signal_array

def sawtooth_signal(amplitude, time,number_saw_tooths):
    # comput one sawtooth
    signal_array = np.zeros_like(time)
    signal_array[0] = -1*amplitude
    # Discretisation of the time array in intervals
    interval_step = len(time)//number_saw_tooths
    time_step = time[interval_step]-time[0]
    signal_array[0:interval_step] = 2*amplitude*(time[0:interval_step]- time[0]-float(time_step)/2)/time_step
    start = interval_step
    for interval in range(1, number_saw_tooths):
        signal_array[start:start+interval_step] = signal_array[0:interval_step]
        start += interval_step
    return signal_array
    