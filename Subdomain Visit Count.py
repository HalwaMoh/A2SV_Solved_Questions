class Solution:
    def subdomainVisits(self, cpdomains):
        counts = {} 

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            parts = domain.split(".")
            
            
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counts[subdomain] = counts.get(subdomain, 0) + count

        
        return ["{} {}".format(cnt, dom) for dom, cnt in counts.items()]
