using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SmartLog.Biz
{
    internal static class DependencyInjection
    {
        public static IServiceCollection AddBiz(this IServiceCollection services)
        {

            return services;
        }
    }
}
