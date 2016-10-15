from audio_in import amplitude

if __name__ == "__main__":


    tt = amplitude.Average()

    while True:

        if tt.listen() > 0.01:

            print tt.listen()