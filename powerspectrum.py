def powerspec(data, divisor, N):
        """
        Take the power spectrum of a signal array
        """
        import numpy as np
        import ugradio
        
        Vsamp = 62.5/divisor 
    
        #N = 512 N is samples

        time = np.linspace(-N/(2*Vsamp),(N/2-1)/Vsamp,N)
        #Fourier voltage spectrum - have real and imaginary parts
        # frequency domain signal
        '''The output is a function of frequency, so you have to specify 
        the frequencies for which you want the output. Suggested: make the 
        frequency increment equal to Vsamp/N over a total range of just under
        Vsamp. Thus, you calculate a voltage spectrum running from -Vsamp/2 to
        not quite Vsamp/2.'''
    
        f_input = np.linspace(-Vsamp/2, (Vsamp/2)*(1 - (2/N)),N)
    
        f,fx = ugradio.dft.dft(data[:N],t=time, f = f_input, vsamp=Vsamp)
    
        # Fourier power spectrum
        '''Power is proportional to voltage squared.
        We want the sum of the squares of the real and imaginary parts.'''
    
        Pow = np.abs(fx)**2
    
    
        return Pow, f
