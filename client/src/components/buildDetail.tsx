import * as React from 'react';
import * as _ from 'lodash';

import { BuildModel } from '../models/build';
import Logs from '../containers/logs';
import {
  getBuildUrl,
  getProjectUrl,
  getUserUrl,
  splitUniqueName,
} from '../constants/utils';
import Breadcrumb from './breadcrumb';
import LinkedTab from './linkedTab';
import BuildOverview from './buildOverview';

export interface Props {
  build: BuildModel;
  onDelete: () => any;
  fetchData: () => any;
}

export default class BuildDetail extends React.Component<Props, Object> {
  componentDidMount() {
    this.props.fetchData();
  }

  public render() {
    const build = this.props.build;

    if (_.isNil(build)) {
      return (<div>Nothing</div>);
    }
    let values = splitUniqueName(build.project);
    let buildUrl = getBuildUrl(values[0], values[1], this.props.build.id);
    let breadcrumbLinks = [
      {name: values[0], value: getUserUrl(values[0])},
      {name: values[1], value: getProjectUrl(values[0], values[1])},
      {name: `Build ${build.id}`}];
    return (
      <div className="row">
        <div className="col-md-12">
          <div className="entity-details">
            <Breadcrumb icon="fa-cube" links={breadcrumbLinks}/>
            <LinkedTab
              baseUrl={buildUrl}
              tabs={[
                {
                  title: 'Overview',
                  component: <BuildOverview build={build}/>,
                  relUrl: ''
                }, {
                  title: 'Logs',
                  component: <Logs
                    fetchData={() => null}
                    logs={''}
                    user={build.user}
                    project={build.project}
                    resource="builds"
                    id={build.id}
                  />,
                  relUrl: 'logs'
                }
              ]}
            />
          </div>
        </div>
      </div>
    );
  }
}
