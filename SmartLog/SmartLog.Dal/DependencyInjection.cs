using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SmartLog.Dal
{
    internal static class DependencyInjection
    {
        public static IServiceCollection AddDal(this IServiceCollection services)
        {
            return services;
        }
    }
}
